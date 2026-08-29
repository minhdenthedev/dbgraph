import os
import unittest
from typing import cast

from dbgraph.entity.aspect import (
    RCategoricalStatistics,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RNumericalStatistics,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    SemanticAspect,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType
from dbgraph.persistent.sql_graph_persistent import SQLGraphPersistent


class TestSQLGraphPersistent(unittest.TestCase):
    def setUp(self) -> None:
        self.persistent = SQLGraphPersistent("sqlite:///data/graph.db")
        assets = [
            Asset(
                asset_id="1",
                name="table-1",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="table-1-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-1-statistic", num_rows=0, num_columns=0
                    ),
                    "schema_properties": RTableSchemaAspect(
                        name="table-1-schema", indices={}, pks=[]
                    ),
                },
            ),
            Asset(
                asset_id="2",
                name="table-2",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="table-2-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-2-statistic", num_rows=0, num_columns=0
                    ),
                    "schema_properties": RTableSchemaAspect(
                        name="table-2-schema", indices={}, pks=[]
                    ),
                },
            ),
            Asset(
                asset_id="3",
                name="table-3",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="table-3-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-3-statistic", num_rows=0, num_columns=0
                    ),
                    "schema_properties": RTableSchemaAspect(
                        name="table-3-schema", indices={}, pks=[]
                    ),
                },
            ),
            Asset(
                asset_id="4",
                name="column-1-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-1-1-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-1-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=RNumericalStatistics(min=0, max=0, mean=0),
                        categorical_stats=None,
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-1-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id="5",
                name="column-1-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-1-2-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-1-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2}
                        ),
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-1-2-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id="6",
                name="column-2-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-2-1-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-2-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=RNumericalStatistics(min=0, max=0, mean=0),
                        categorical_stats=None,
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-2-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id="7",
                name="column-2-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-2-2-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-2-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2}
                        ),
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-2-2-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id="8",
                name="column-3-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-3-1-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-3-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=RNumericalStatistics(min=0, max=0, mean=0),
                        categorical_stats=None,
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-3-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id="9",
                name="column-3-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties": SemanticAspect(
                        name="column-3-2-semantic", description="test", keywords=[]
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-3-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2}
                        ),
                    ),
                    "schema_properties": RColumnSchemaAspect(
                        name="column-3-2-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
        ]
        links = [
            Link(
                link_id="1",
                name="table-1-column-1-1",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[3].asset_id,
            ),
            Link(
                link_id="2",
                name="table-1-column-1-2",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[4].asset_id,
            ),
            Link(
                link_id="3",
                name="table-2-column-2-1",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[5].asset_id,
            ),
            Link(
                link_id="4",
                name="table-2-column-2-2",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[6].asset_id,
            ),
            Link(
                link_id="5",
                name="table-3-column-3-1",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[7].asset_id,
            ),
            Link(
                link_id="6",
                name="table-3-column-3-2",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[8].asset_id,
            ),
            Link(
                link_id="7",
                name="table-1-table-2",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[0].asset_id,
                destination_id=assets[1].asset_id,
                aspects={
                    "foreign_key_properties": RForeignKeyAspect(
                        name="table-1-table-2-fk",
                        from_column="fake_col_1",
                        to_column="fake_col_2",
                        on_delete="CASCADE",
                        on_update="CASCADE",
                    )
                },
            ),
            Link(
                link_id="8",
                name="table-2-table-3",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[1].asset_id,
                destination_id=assets[2].asset_id,
                aspects={
                    "foreign_key_properties": RForeignKeyAspect(
                        name="table-1-table-2-fk",
                        from_column="fake_col_1",
                        to_column="fake_col_2",
                        on_delete="CASCADE",
                        on_update="CASCADE",
                    )
                },
            ),
        ]
        self.graph = DatabaseGraph(assets, links)
        self.graph_id = "1"
        self.graph_name = "graph-1"
        self.persistent.create_graph(self.graph_id, self.graph_name)

    def tearDown(self) -> None:
        self.persistent.delete_graph(self.graph_id)
        os.remove("data/graph.db")

    def test_asset(self):
        target_asset = self.graph.get_asset("1")
        self.persistent.insert_asset(target_asset, self.graph_id)

        asset = self.persistent.get_asset(target_asset.asset_id, self.graph_id)
        self.assertEqual(asset.asset_id, "1")
        self.assertTrue("semantic_properties" in asset.aspects)
        self.assertEqual(asset.aspects["semantic_properties"].name, "table-1-semantic")
        self.assertEqual(asset.aspects, target_asset.aspects)
        self.persistent.remove_asset("1", self.graph_id)
        with self.assertRaises(KeyError):
            asset = self.persistent.get_asset("1", self.graph_id)

    def test_link(self):
        target_link = self.graph.get_link("1", "2")
        self.persistent.insert_link(target_link, self.graph_id)

        link = self.persistent.get_link(target_link.link_id, self.graph_id)
        self.assertEqual(link.link_id, "7")
        self.assertTrue("foreign_key_properties" in link.aspects)
        self.assertEqual(
            link.aspects["foreign_key_properties"].name, "table-1-table-2-fk"
        )
        self.persistent.remove_link(link.link_id, self.graph_id)
        with self.assertRaises(KeyError):
            link = self.persistent.get_link(link.link_id, self.graph_id)

    def test_get_aspects_of_asset_table(self):
        target_asset = self.graph.get_asset("1")
        self.persistent.insert_asset(target_asset, self.graph_id)
        aspects = self.persistent.get_aspects_of_asset("1")
        self.assertTrue("statistical_properties" in aspects)
        self.assertTrue("schema_properties" in aspects)
        self.assertTrue("semantic_properties" in aspects)
        self.assertIsInstance(aspects["statistical_properties"], RTableStatisticsAspect)
        self.assertIsInstance(aspects["schema_properties"], RTableSchemaAspect)
        self.assertIsInstance(aspects["semantic_properties"], SemanticAspect)
        stats_aspect = cast(RTableStatisticsAspect, aspects["statistical_properties"])
        schema_aspect = cast(RTableSchemaAspect, aspects["schema_properties"])
        semantic_aspect = cast(SemanticAspect, aspects["semantic_properties"])
        self.assertEqual(stats_aspect.num_rows, 0)
        self.assertEqual(stats_aspect.num_columns, 0)
        self.assertEqual(stats_aspect.name, "table-1-statistic")
        self.assertEqual(schema_aspect.name, "table-1-schema")
        self.assertEqual(semantic_aspect.name, "table-1-semantic")
        self.persistent.remove_asset(target_asset.asset_id, self.graph_id)

    def test_get_aspects_of_asset_numerical_column(self):
        target_asset = self.graph.get_asset("6")
        self.persistent.insert_asset(target_asset, self.graph_id)
        aspects = self.persistent.get_aspects_of_asset("6")
        self.assertTrue("statistical_properties" in aspects)
        self.assertTrue("schema_properties" in aspects)
        self.assertTrue("semantic_properties" in aspects)
        self.assertIsInstance(
            aspects["statistical_properties"], RColumnStatisticsAspect
        )
        self.assertIsInstance(aspects["schema_properties"], RColumnSchemaAspect)
        self.assertIsInstance(aspects["semantic_properties"], SemanticAspect)
        stats_aspect = cast(RColumnStatisticsAspect, aspects["statistical_properties"])
        schema_aspect = cast(RColumnSchemaAspect, aspects["schema_properties"])
        semantic_aspect = cast(SemanticAspect, aspects["semantic_properties"])
        self.assertEqual(stats_aspect.name, "column-2-1-statistic")
        self.assertEqual(schema_aspect.name, "column-2-1-schema")
        self.assertEqual(semantic_aspect.name, "column-2-1-semantic")
        self.assertIsInstance(stats_aspect.numerical_stats, RNumericalStatistics)
        self.assertEqual(stats_aspect.numerical_stats.min, 0)  # pyright: ignore[reportOptionalMemberAccess]
        self.persistent.remove_asset(target_asset.asset_id, self.graph_id)

    def test_get_aspects_of_asset_categorical_column(self):
        target_asset = self.graph.get_asset("7")
        self.persistent.insert_asset(target_asset, self.graph_id)
        aspects = self.persistent.get_aspects_of_asset("7")
        self.assertTrue("statistical_properties" in aspects)
        self.assertTrue("schema_properties" in aspects)
        self.assertTrue("semantic_properties" in aspects)
        self.assertIsInstance(
            aspects["statistical_properties"], RColumnStatisticsAspect
        )
        self.assertIsInstance(aspects["schema_properties"], RColumnSchemaAspect)
        self.assertIsInstance(aspects["semantic_properties"], SemanticAspect)
        stats_aspect = cast(RColumnStatisticsAspect, aspects["statistical_properties"])
        schema_aspect = cast(RColumnSchemaAspect, aspects["schema_properties"])
        semantic_aspect = cast(SemanticAspect, aspects["semantic_properties"])
        self.assertEqual(stats_aspect.name, "column-2-2-statistic")
        self.assertEqual(schema_aspect.name, "column-2-2-schema")
        self.assertEqual(semantic_aspect.name, "column-2-2-semantic")
        self.assertIsInstance(stats_aspect.categorical_stats, RCategoricalStatistics)
        self.assertEqual(stats_aspect.categorical_stats.value_counts, {"1": 1, "2": 2})  # pyright: ignore[reportOptionalMemberAccess]
        self.persistent.remove_asset(target_asset.asset_id, self.graph_id)

    def test_get_aspects_of_link(self):
        link = self.graph.get_link("1", "2")
        self.persistent.insert_link(link, self.graph_id)
        aspects = self.persistent.get_aspects_of_link(link.link_id)
        self.assertTrue("foreign_key_properties" in aspects)
        self.assertIsInstance(aspects["foreign_key_properties"], RForeignKeyAspect)
        fk_aspect = cast(RForeignKeyAspect, aspects["foreign_key_properties"])
        self.assertEqual(fk_aspect.from_column, "fake_col_1")
        self.assertEqual(fk_aspect.to_column, "fake_col_2")
        self.assertEqual(fk_aspect.on_delete, "CASCADE")
        self.assertEqual(fk_aspect.on_update, "CASCADE")
        self.persistent.remove_link(link.link_id, self.graph_id)

    def test_insert_assets(self):
        self.persistent.insert_assets(self.graph.assets, self.graph_id)
        self.persistent.remove_assets(
            [asset.asset_id for asset in self.graph.assets], self.graph_id
        )

    def test_insert_links(self):
        self.persistent.insert_links(self.graph.links, self.graph_id)
        self.persistent.remove_links(
            [link.link_id for link in self.graph.links], self.graph_id
        )

    def test_get_assets(self):
        self.persistent.insert_assets(self.graph.assets, self.graph_id)
        assets = self.persistent.get_assets(self.graph_id)
        self.persistent.remove_assets(
            [asset.asset_id for asset in self.graph.assets], self.graph_id
        )
        self.assertEqual(assets, self.graph.assets)

    def test_get_links(self):
        self.persistent.insert_links(self.graph.links, self.graph_id)
        links = self.persistent.get_links(self.graph_id)
        self.persistent.remove_links(
            [link.link_id for link in self.graph.links], self.graph_id
        )
        self.assertEqual(links, self.graph.links)

    def test_load_graph(self):
        self.persistent.insert_assets(self.graph.assets, self.graph_id)
        self.persistent.insert_links(self.graph.links, self.graph_id)
        graph = self.persistent.load_graph(self.graph_id)
        self.assertEqual(graph, self.graph)

    def test_get_graph_info(self):
        graph_info = self.persistent.get_graph_info("1")
        self.assertEqual(graph_info[1], "graph-1")
        self.assertEqual(graph_info[2], False)


if __name__ == "__main__":
    unittest.main()
