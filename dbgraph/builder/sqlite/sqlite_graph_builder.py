import sqlite3
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from dbgraph.builder.graph_builder import GraphBuilder
from dbgraph.entity.aspect import (
    RCategoricalStatistics,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RNumericalStatistics,
    RTableSchemaAspect,
    RTableStatisticsAspect,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


@dataclass
class SQLiteGraphBuilder(GraphBuilder):
    """Building graph for SQLite database"""

    db_path: Path

    def __post_init__(self):
        self.columns_assets: dict[str, list[Asset]] = {}
        self.tables_assets: dict[str, Asset] = {}

    def _get_tables_names(self) -> list[str]:
        sql = """
        SELECT name
        FROM sqlite_schema
        WHERE type='table'
          AND name NOT LIKE 'sqlite_%';
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(sql)
            rows = cur.fetchall()
            return [r[0] for r in rows]

    def _get_numeric_column_stats(
        self, column_name: str, table_name: str
    ) -> RNumericalStatistics:
        sql = f"""
            SELECT MIN({column_name}), MAX({column_name}), AVG({column_name})
            FROM "{table_name}"
            WHERE {column_name} IS NOT NULL;
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(sql)
            row = cur.fetchone()
            return RNumericalStatistics(min=row[0], max=row[1], mean=row[2])

    def _get_categorical_column_stats(
        self, column_name: str, table_name: str
    ) -> RCategoricalStatistics:
        sql = f"""
            SELECT {column_name}, COUNT(*) as frequency
            FROM {table_name}
            WHERE {column_name} IS NOT NULL
            GROUP BY {column_name}
            ORDER BY frequency DESC
            LIMIT 10;
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(sql)
            rows = cur.fetchall()
            counts_dict = {str(row[0]): int(row[1]) for row in rows}
            return RCategoricalStatistics(value_counts=counts_dict)

    def _get_column_null_metrics(
        self, column_name: str, table_name: str
    ) -> tuple[int, int]:
        query = f"""
            SELECT
                COUNT({column_name}) as non_null_count,
                SUM(CASE WHEN {column_name} IS NULL THEN 1 ELSE 0 END) as null_count,
                COUNT(*) as total_rows
            FROM "{table_name}";
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()

        # Handle the edge case where a table is completely empty (returns None or 0s)
        non_null = row[0] if row[0] is not None else 0
        nulls = row[1] if row[1] is not None else 0
        return non_null, nulls

    def _get_column_stats_aspect(
        self, column_asset: Asset, table_name: str
    ) -> RColumnStatisticsAspect:
        if column_asset.type != AssetType.RCOLUMN:
            raise ValueError("Input asset is not RCOLUMN type.")
        if "schema_properties" in column_asset.aspects:
            aspect_name = f"{column_asset.name}_column_stats"
            non_null, nulls = self._get_column_null_metrics(
                column_asset.name, table_name
            )
            if isinstance(
                column_asset.aspects["schema_properties"], RColumnSchemaAspect
            ):
                dtype = column_asset.aspects["schema_properties"].dtype
                if dtype == "INTEGER" or dtype == "REAL":
                    num_stats = self._get_numeric_column_stats(
                        column_asset.name, table_name
                    )
                    cat_stats = None
                elif dtype == "TEXT":
                    cat_stats = self._get_categorical_column_stats(
                        column_asset.name, table_name
                    )
                    num_stats = None
                else:
                    num_stats = None
                    cat_stats = None
                return RColumnStatisticsAspect(
                    name=aspect_name,
                    null_count=nulls,
                    non_null_count=non_null,
                    numerical_stats=num_stats,
                    categorical_stats=cat_stats,
                )
            else:
                raise TypeError(
                    "schema_properties is not an instance of RColumnSchemaAspect"
                )
        else:
            raise RuntimeError("Please prepare schema_properties first!")

    def _get_columns_assets(self, table_name: str) -> list[Asset]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(f'PRAGMA table_info("{table_name}");')
            rows = cur.fetchall()
        assets = []
        for row in rows:
            schema_aspect = RColumnSchemaAspect(
                name=f"{row[1]}_column_schema",
                dtype=row[2],
                is_nullable=(row[3] == 0),
                is_pk=(row[5] == 1),
            )
            asset = Asset(
                asset_id=str(uuid4()),
                name=row[1],
                type=AssetType.RCOLUMN,
                aspects={"schema_properties": schema_aspect},
            )
            stats_aspect = self._get_column_stats_aspect(asset, table_name)
            asset.aspects["statistical_properties"] = stats_aspect
            assets.append(asset)
        return assets

    def _get_table_nrows(self, table_name: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(f'SELECT COUNT(*) FROM "{table_name}";')
            nrow = cur.fetchone()[0]
        return nrow

    def _get_table_schema_aspect(
        self, table_name: str, columns_assets: list[Asset]
    ) -> RTableSchemaAspect:
        indices_map = {}
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(f'PRAGMA index_list("{table_name}");')
            index_list = cursor.fetchall()

            # 3. For each index, fetch the columns it covers
            for idx in index_list:
                index_name = idx[1]
                # Skip internal/implicit auto-indexes if you only want explicitly created ones,
                # but usually it's best to include them to capture implicit UNIQUE constraints.
                if index_name.startswith("sqlite_autoindex"):
                    continue

                cursor.execute(f"PRAGMA index_info({index_name});")
                index_info = cursor.fetchall()

                # Map the index name to its associated columns (row[2] is the column name)
                columns_in_index = [row[2] for row in index_info if row[2]]
                indices_map[index_name] = columns_in_index
        pks = []
        for asset in columns_assets:
            if "schema_properties" in asset.aspects:
                schema_aspect = asset.aspects["schema_properties"]
                if isinstance(schema_aspect, RColumnSchemaAspect):
                    if schema_aspect.is_pk:
                        pks.append(asset.name)
        return RTableSchemaAspect(
            name=f"{table_name}_table_schema", pks=pks, indices=indices_map
        )

    def _build_assets(self) -> list[Asset]:
        tables = self._get_tables_names()
        columns_assets = {table: self._get_columns_assets(table) for table in tables}
        assets = []
        for table in tables:
            nrow = self._get_table_nrows(table)
            ncol = len(columns_assets[table])
            stats_aspect = RTableStatisticsAspect(
                name=f"{table}_table_stats", num_rows=nrow, num_columns=ncol
            )
            schema_aspect = self._get_table_schema_aspect(table, columns_assets[table])
            table_asset = Asset(
                asset_id=str(uuid4()),
                name=table,
                type=AssetType.RTABLE,
                aspects={
                    "schema_properties": schema_aspect,
                    "statistical_properties": stats_aspect,
                },
            )
            assets.append(table_asset)
            self.columns_assets[table_asset.name] = columns_assets[table]
            self.tables_assets[table_asset.name] = table_asset
        for assets_list in columns_assets.values():
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
        tables = [a for a in self.tables_assets.keys()]
        links = []
        with sqlite3.connect(self.db_path) as conn:
            for table_name in tables:
                cur = conn.execute(f'PRAGMA foreign_key_list("{table_name}");')
                fk_rows = cur.fetchall()

                for row in fk_rows:
                    from_table = table_name
                    from_column = row[3]
                    to_table = row[2]
                    to_column = row[4]
                    on_update = row[5]
                    on_delete = row[6]
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
                                from_column=from_column,
                                to_column=to_column,
                                on_delete=on_delete,
                                on_update=on_update,
                            )
                        },
                    )
                    links.append(link)
        return links

    def _build_links(self) -> list[Link]:
        contain_links = self._build_contain_links()
        fk_links = self._build_fk_links()
        return contain_links + fk_links
