from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import (
    Column,
    MetaData,
    Numeric,
    PrimaryKeyConstraint,
    String,
    Table,
    create_engine,
    func,
    inspect,
    select,
    SmallInteger,
    Integer,
    BigInteger,
    Float,
    DECIMAL,
    Text,
    Unicode,
    UnicodeText,
    CHAR,
    NCHAR,
    BLOB,
    DATE,
    DATETIME,
    distinct,
)
from sqlalchemy.orm import Session

from dbgraph.builder.graph_builder import GraphBuilder
from dbgraph.entity.aspect import (
    RCategoricalStatistics,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RNumericalStatistics,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    RTemporalStatistics,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


@dataclass
class SQLGraphBuilder(GraphBuilder):
    """Build the database graph using SQL Alchemy"""

    db_uri: str
    max_worker: int = 4

    def __post_init__(self):
        self.engine = create_engine(self.db_uri)
        self.columns_assets: dict[str, list[Asset]] = {}
        self.tables_assets: dict[str, Asset] = {}
        self._tables_orm: dict[str, Table] = {
            table.name: table for table in self._orm_tables
        }

    @property
    def _orm_tables(self) -> list[Table]:
        orm_tables = []
        for table_name in self.table_names:
            metadata = MetaData()
            table = Table(table_name, metadata, autoload_with=self.engine)
            orm_tables.append(table)
        return orm_tables

    @property
    def table_names(self) -> list[str]:
        inspector = inspect(self.engine)
        return inspector.get_table_names()

    def _get_numerical_stats_aspect(self, col: Column) -> RNumericalStatistics:
        stmt = select(
            func.min(col).label("min"),
            func.max(col).label("max"),
            func.avg(col).label("mean"),
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).one()
        return RNumericalStatistics(
            min=float(result.min), max=float(result.max), mean=float(result.mean)
        )

    def _get_null_info(self, col: Column) -> tuple[int, int]:
        stmt = select(
            func.count(col).label("non_null_count"),
            (func.count() - func.count(col)).label("null_count"),
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).one()
        return int(result.non_null_count), int(result.null_count)

    def _get_cat_stats_aspect(self, col: Column) -> RCategoricalStatistics:
        stmt = (
            select(
                col.label("value"),
                func.count().label("value_count"),
            )
            .where(col.is_not(None))
            .group_by(col)
            .order_by(func.count().desc())
            .limit(10)
        )
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
        value_counts = {str(row[0]): int(row[1]) for row in rows}
        return RCategoricalStatistics(value_counts)

    def _get_temp_aspect(self, col: Column) -> RTemporalStatistics:
        min_max_nunique_stmt = select(
            func.min(col), func.max(col), func.count(distinct(col))
        )
        mode_stmt = select(col).group_by(col).order_by(func.count(col).desc()).limit(1)
        with Session(self.engine) as session:
            min_time, max_time, nunique = session.execute(min_max_nunique_stmt).one()
            mode = session.execute(mode_stmt).scalar()
        return RTemporalStatistics(min_time, max_time, mode, nunique)

    def _get_stats_aspect(self, col: Column) -> RColumnStatisticsAspect:
        non_null_count, null_count = self._get_null_info(col)
        num_aspect = None
        cat_aspect = None
        temp_aspect = None
        if isinstance(
            col.type, (Numeric, Integer, SmallInteger, BigInteger, Float, DECIMAL)
        ):
            num_aspect = self._get_numerical_stats_aspect(col)
        elif isinstance(col.type, (String, Text, Unicode, UnicodeText, CHAR, NCHAR)):
            cat_aspect = self._get_cat_stats_aspect(col)
        elif isinstance(col.type, (DATE, DATETIME)):
            temp_aspect = self._get_temp_aspect(col)
        elif isinstance(col.type, (BLOB,)):
            pass
        else:
            raise NotImplementedError(
                f"Only support Numeric, String, Date, and BLOB. Got {col.type} for {col.name}"
            )
        return RColumnStatisticsAspect(
            name=f"{col.name}_column_stats",
            numerical_stats=num_aspect,
            categorical_stats=cat_aspect,
            temporal_stats=temp_aspect,
            non_null_count=non_null_count,
            null_count=null_count,
        )

    def _make_column_asset(self, col: Column, pks: PrimaryKeyConstraint) -> Asset:
        schema_aspect = RColumnSchemaAspect(
            name=f"{col.name}_column_schema",
            dtype=str(col.type),
            is_nullable=col.nullable or False,
            is_pk=col.name in [c.name for c in pks.columns],
        )
        stats_aspect = self._get_stats_aspect(col)
        return Asset(
            asset_id=str(uuid4()),
            name=col.name,
            type=AssetType.RCOLUMN,
            aspects={
                "schema_properties": schema_aspect,
                "statistical_properties": stats_aspect,
            },
        )

    def _get_columns_assets(self, table_name: str) -> list[Asset]:
        table = self._tables_orm[table_name]
        assets = []
        pks = table.primary_key
        with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            assets = list(
                executor.map(
                    self._make_column_asset, table.columns, [pks] * len(table.columns)
                )
            )
        return assets

    def _get_table_stats_aspect(self, table_name: str) -> RTableStatisticsAspect:
        table = self._tables_orm[table_name]
        nrow = self._get_table_nrow(table_name)
        ncol = len(table.columns)
        return RTableStatisticsAspect(
            name=f"{table.name}_table_stats", num_rows=nrow, num_columns=ncol
        )

    def _get_table_nrow(self, table_name: str) -> int:
        table = self._tables_orm[table_name]

        stmt = select(func.count()).select_from(table)

        with self.engine.connect() as conn:
            nrow = conn.execute(stmt).scalar()
        if nrow is None:
            raise RuntimeError("Can't get number of row")
        return int(nrow)

    def _get_table_schema_aspect(self, table_name: str) -> RTableSchemaAspect:
        table = self._tables_orm[table_name]
        pks = [c.name for c in table.primary_key.columns]
        indices = {str(i.name): [c.name for c in i.columns] for i in table.indexes}

        return RTableSchemaAspect(
            name=f"{table_name}_table_schema", pks=pks, indices=indices
        )

    def _make_table_asset(self, table_name: str) -> Asset:
        stats_aspect = self._get_table_stats_aspect(table_name)
        schema_aspect = self._get_table_schema_aspect(table_name)
        table_asset = Asset(
            asset_id=str(uuid4()),
            name=table_name,
            type=AssetType.RTABLE,
            aspects={
                "schema_properties": schema_aspect,
                "statistical_properties": stats_aspect,
            },
        )
        self.columns_assets[table_asset.name] = self._get_columns_assets(table_name)
        self.tables_assets[table_asset.name] = table_asset
        return table_asset

    def _build_assets(self) -> list[Asset]:
        with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            assets = list(executor.map(self._make_table_asset, self.table_names))
        for assets_list in self.columns_assets.values():
            assets.extend(assets_list)
        return assets

    def _build_contain_links(self) -> list[Link]:
        contain_links = []
        for table_name, columns_assets in self.columns_assets.items():
            table_asset = self.tables_assets[table_name]
            for column_asset in columns_assets:
                link = Link(
                    link_id=str(uuid4()),
                    name=f"{table_asset.name}_{column_asset.name}",
                    source_id=table_asset.asset_id,
                    destination_id=column_asset.asset_id,
                    type=LinkType.CONTAIN,
                )
                contain_links.append(link)
        return contain_links

    def _build_fk_links(self) -> list[Link]:
        links = []
        for table_name in self.tables_assets:
            table = self._tables_orm[table_name]
            for fk in table.foreign_keys:
                to_table = fk.column.table.name
                from_table = table.name
                name = f"{from_table}_{to_table}_fk"
                link = Link(
                    link_id=str(uuid4()),
                    name=name,
                    source_id=self.tables_assets[from_table].asset_id,
                    destination_id=self.tables_assets[to_table].asset_id,
                    type=LinkType.FOREIGN_KEY,
                    aspects={
                        "foreign_key_properties": RForeignKeyAspect(
                            name=name,
                            from_column=fk.parent.name,
                            to_column=fk.column.name,
                            on_delete=fk.ondelete or "",
                            on_update=fk.onupdate or "",
                        )
                    },
                )
                links.append(link)
        return links

    def _build_links(self) -> list[Link]:
        contain_links = self._build_contain_links()
        fk_links = self._build_fk_links()
        return contain_links + fk_links
