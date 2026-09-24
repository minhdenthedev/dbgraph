import logging
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from unittest import result
from uuid import uuid4
from tqdm import tqdm

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
    TIME, TIMESTAMP,
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
from dbgraph.utils.logging import console_handler, file_handler

logger = logging.getLogger("SQLGraphBuilder")
logger.addHandler(console_handler)


@dataclass
class SQLGraphBuilder(GraphBuilder):
    """Build the database graph using SQL Alchemy

    Attributes:
        db_uri: URI to source database
        max_worker: number of parallel workers to process
    """

    db_uri: str
    max_worker: int = 4
    use_tqdm: bool = False
    detector_sample_size: int = 200
    textual_length_threshold: int = 30
    textual_distinct_ratio_threshold: float = 0.8

    def __post_init__(self):
        logger.info("Creating SQLAlchemy engine...")
        self.engine = create_engine(
            self.db_uri,
        )
        logger.info("Engine created!")
        self.columns_assets: dict[str, list[Asset]] = {}
        self.tables_assets: dict[str, Asset] = {}
        self.metadata = MetaData()
        self.inspector = inspect(self.engine)

    def _get_column_orm(self, table_name: str, column_name: str) -> Column:
        table = self._get_table_orm(table_name)
        for column in table.columns:
            if column.name == column_name:
                return column
        raise KeyError(f"Column `{column_name}` not found in table `{table_name}`")

    def _get_table_orm(self, table_name: str) -> Table:
        """Fast operation the `Table` object of
        SQLAlchemy

        """
        try:
            logger.debug("Getting table `%s` from memory...", table_name)
            return self.metadata.tables[table_name]
        except KeyError:
            logger.debug(
                "Failed to get table `%s` from memory. Getting it from source DB...",
                table_name,
            )
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            return table

    @property
    def table_names(self) -> list[str]:
        """Fast operation to get table names"""
        return self.inspector.get_table_names()

    def _get_numerical_stats_aspect(self, col: Column) -> RNumericalStatistics:
        stmt = select(
            func.min(col).label("min"),
            func.max(col).label("max"),
            func.avg(col).label("mean"),
        )
        with self.engine.connect() as conn:
            logger.debug(
                "`%s` - get numerical stats", col,
            )
            result = conn.execute(stmt).one()
        return RNumericalStatistics(
            min=float(result.min), max=float(result.max), mean=float(result.mean),
        )

    def _get_null_info(self, col: Column) -> tuple[int, int]:
        stmt = select(
            func.count(col).label("non_null_count"),
            (func.count() - func.count(col)).label("null_count"),
        )
        with self.engine.connect() as conn:
            logger.debug("`%s` - get null info", col)
            result = conn.execute(stmt).one()
        return int(result.non_null_count), int(result.null_count)

    def _is_column_textual(self, col: Column) -> bool:
        sample = (
            select(col)
            .where(col.isnot(None))
            .limit(self.detector_sample_size)  # lấy số lượng mong muốn
        ).subquery()
        avg_char_length_stmt = select(
            func.avg(func.length(sample.c[col.name])),
        )
        distinct_count_stmt = select(
            func.count(func.distinct(sample.c[col.name]))
        )

        with self.engine.connect() as conn:
            avg_char_length = conn.execute(avg_char_length_stmt).one()[0]
            if avg_char_length is None:
                return False
            if avg_char_length > self.textual_length_threshold:
                return True
            distinct_count = conn.execute(distinct_count_stmt).one()[0]
            if distinct_count is None:
                return False
            if ((
                    distinct_count / self.detector_sample_size) >
                    self.textual_distinct_ratio_threshold):
                return True
        return False

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
            logger.debug("`%s` - get categorical stats", col)
            rows = conn.execute(stmt).all()
        value_counts = {str(row[0]): int(row[1]) for row in rows}
        return RCategoricalStatistics(value_counts)

    def _get_temp_aspect(self, col: Column) -> RTemporalStatistics:
        min_max_nunique_stmt = select(
            func.min(col), func.max(col), func.count(distinct(col)),
        )
        mode_stmt = select(col).group_by(col).order_by(func.count(col).desc()).limit(1)
        with Session(self.engine) as session:
            logger.debug("`%s` - get temporal stats", col)
            min_time, max_time, nunique = session.execute(min_max_nunique_stmt).one()
            mode = session.execute(mode_stmt).scalar()
        return RTemporalStatistics(min_time, max_time, mode, nunique)

    def _get_stats_aspect(self, col: Column) -> RColumnStatisticsAspect:
        logger.debug("`%s` - building statistical aspect...", col)
        non_null_count, null_count = self._get_null_info(col)
        num_aspect = None
        cat_aspect = None
        temp_aspect = None
        is_textual = False
        if isinstance(
                col.type, (Numeric, Integer, SmallInteger, BigInteger, Float, DECIMAL),
        ):
            num_aspect = self._get_numerical_stats_aspect(col)
        elif isinstance(col.type, (String, Text, Unicode, UnicodeText, CHAR, NCHAR)):
            is_textual = self._is_column_textual(col)
            if is_textual:
                logger.debug("`%s` is textual type", col)
                cat_aspect = None
            else:
                cat_aspect = self._get_cat_stats_aspect(col)
        elif isinstance(col.type, (DATE, DATETIME, TIME, TIMESTAMP)):
            temp_aspect = self._get_temp_aspect(col)
        elif isinstance(col.type, (BLOB,)):
            pass
        else:
            raise NotImplementedError(
                f"Only support Numeric, String, Date, and BLOB. Got {col.type} for "
                f"{col}",
            )
        return RColumnStatisticsAspect(
            name=f"{col.name}_column_stats",
            numerical_stats=num_aspect,
            is_textual=is_textual,
            categorical_stats=cat_aspect,
            temporal_stats=temp_aspect,
            non_null_count=non_null_count,
            null_count=null_count,
        )

    def _make_column_asset(self, col: Column, pks: PrimaryKeyConstraint) -> Asset:
        logger.info("`%s` - building column asset...", col)
        schema_aspect = RColumnSchemaAspect(
            name=f"{col.name}_column_schema",
            dtype=str(col.type),
            is_nullable=col.nullable or False,
            is_pk=col.name in [c.name for c in pks.columns],
        )
        stats_aspect = self._get_stats_aspect(col)
        return Asset(
            asset_id=uuid4(),
            name=col.name,
            type=AssetType.RCOLUMN,
            aspects={
                "schema_properties"     : schema_aspect,
                "statistical_properties": stats_aspect,
            },
        )

    def _get_columns_assets(self, table_name: str) -> list[Asset]:
        logger.info("`%s` - building columns...", table_name)
        table = self._get_table_orm(table_name)
        assets = []
        pks = table.primary_key
        for column in table.columns:
            assets.append(self._make_column_asset(column, pks))
        # with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
        #     if self.use_tqdm:
        #         assets = list(
        #             tqdm(
        #                 executor.map(
        #                     self._make_column_asset, table.columns,
        #                     [pks] * len(table.columns),
        #                 ),
        #                 total=len(table.columns),
        #                 desc="Processing columns",
        #             ),
        #         )
        #     else:
        #         assets = list(
        #             executor.map(
        #                 self._make_column_asset, table.columns,
        #                 [pks] * len(table.columns),
        #             ),
        #         )
        return assets

    def _get_table_stats_aspect(self, table_name: str) -> RTableStatisticsAspect:
        logger.debug("`%s` - building table statistics...", table_name)
        table = self._get_table_orm(table_name)
        row_count = self._get_row_count(table_name)
        col_count = len(table.columns)
        return RTableStatisticsAspect(
            name=f"{table.name}_table_stats", num_rows=row_count, num_columns=col_count,
        )

    def _get_row_count(self, table_name: str) -> int:
        logger.debug("`%s` - get row count...", table_name)
        table = self._get_table_orm(table_name)

        stmt = select(func.count()).select_from(table)

        with self.engine.connect() as conn:
            row_count = conn.scalar(stmt)
        if row_count is None:
            raise RuntimeError("Can't get number of row")
        if not isinstance(row_count, int):
            raise TypeError(
                f"Invalid type for row count:\n\ttype={type(row_count)}\n\tvalue="
                f"{row_count}",
            )
        return row_count

    def _get_table_schema_aspect(self, table_name: str) -> RTableSchemaAspect:
        logger.debug("`%s` - getting schema...", table_name)
        table = self._get_table_orm(table_name)
        pks = [c.name for c in table.primary_key.columns]
        indices = {str(i.name): [c.name for c in i.columns] for i in table.indexes}

        return RTableSchemaAspect(
            name=f"{table_name}_table_schema", pks=pks, indices=indices,
        )

    def _make_table_asset(self, table_name: str) -> Asset:
        logger.info("`%s` - creating table asset...", table_name)
        stats_aspect = self._get_table_stats_aspect(table_name)
        schema_aspect = self._get_table_schema_aspect(table_name)
        table_asset = Asset(
            asset_id=uuid4(),
            name=table_name,
            type=AssetType.RTABLE,
            aspects={
                "schema_properties"     : schema_aspect,
                "statistical_properties": stats_aspect,
            },
        )
        self.columns_assets[table_asset.name] = self._get_columns_assets(table_name)
        self.tables_assets[table_asset.name] = table_asset
        return table_asset

    def _build_assets(self) -> list[Asset]:
        logger.info("creating assets...")
        # with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
        #     assets = list(executor.map(self._make_table_asset, self.table_names))
        assets = []
        for table in self.table_names:
            assets.append(self._make_table_asset(table))
        for assets_list in self.columns_assets.values():
            assets.extend(assets_list)
        return assets

    def _build_contain_links(self) -> list[Link]:
        logger.info("creating contain links...")
        contain_links = []
        for table_name, columns_assets in self.columns_assets.items():
            table_asset = self.tables_assets[table_name]
            for column_asset in columns_assets:
                link = Link(
                    link_id=uuid4(),
                    name=f"{table_asset.name}_{column_asset.name}",
                    source_id=table_asset.asset_id,
                    destination_id=column_asset.asset_id,
                    type=LinkType.CONTAIN,
                )
                contain_links.append(link)
        return contain_links

    def _build_fk_links(self) -> list[Link]:
        logger.info("creating foreign key links...")
        links = []
        for table_name in self.tables_assets:
            table = self._get_table_orm(table_name)
            for fk in table.foreign_keys:
                to_table = fk.column.table.name
                from_table = table.name
                name = f"{from_table}_{to_table}_fk"
                link = Link(
                    link_id=uuid4(),
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
                        ),
                    },
                )
                links.append(link)
        return links

    def _build_links(self) -> list[Link]:
        logger.info("creating links...")
        contain_links = self._build_contain_links()
        fk_links = self._build_fk_links()
        return contain_links + fk_links
