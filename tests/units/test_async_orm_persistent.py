import unittest
import uuid
from datetime import datetime

from dbgraph import Asset, AssetType, Link, LinkType, DatabaseGraph
from dbgraph.entity.aspect import (
    SemanticAspect, RTableStatisticsAspect,
    RTableSchemaAspect, RColumnStatisticsAspect, RNumericalStatistics,
    RColumnSchemaAspect, RCategoricalStatistics, RTemporalStatistics, RForeignKeyAspect,
)
from dbgraph.persistent.async_orm_persistent import async_persistent
from dbgraph.persistent.graph_not_found import GraphNotFound


class TestAsyncOrmPersistent(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        assets = [
            Asset(
                asset_id=uuid.uuid4(),
                name="table-1",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="table-1-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-1-statistic", num_rows=0, num_columns=0,
                    ),
                    "schema_properties"     : RTableSchemaAspect(
                        name="table-1-schema", indices={}, pks=[],
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="table-2",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="table-2-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-2-statistic", num_rows=0, num_columns=0,
                    ),
                    "schema_properties"     : RTableSchemaAspect(
                        name="table-2-schema", indices={}, pks=[],
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="table-3",
                type=AssetType.RTABLE,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="table-3-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RTableStatisticsAspect(
                        name="table-3-statistic", num_rows=0, num_columns=0,
                    ),
                    "schema_properties"     : RTableSchemaAspect(
                        name="table-3-schema", indices={}, pks=[],
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-1-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-1-1-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-1-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        is_textual=False,
                        numerical_stats=RNumericalStatistics(min=0, max=0, mean=0),
                        categorical_stats=None,
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
                        name="column-1-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-1-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-1-2-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-1-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        is_textual=False,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2},
                        ),
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
                        name="column-1-2-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-2-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-2-1-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-2-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        is_textual=False,
                        numerical_stats=None,
                        categorical_stats=None,
                        temporal_stats=RTemporalStatistics(
                            min_time=datetime.now(),
                            max_time=datetime.now(),
                            mode_time=datetime.now(),
                            num_uniques=3,
                        ),
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
                        name="column-2-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-2-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-2-2-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-2-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2},
                        ),
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
                        name="column-2-2-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-3-1",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-3-1-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-3-1-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=RNumericalStatistics(min=0, max=0, mean=0),
                        categorical_stats=None,
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
                        name="column-3-1-schema",
                        dtype="TEXT",
                        is_nullable=False,
                        is_pk=False,
                    ),
                },
            ),
            Asset(
                asset_id=uuid.uuid4(),
                name="column-3-2",
                type=AssetType.RCOLUMN,
                aspects={
                    "semantic_properties"   : SemanticAspect(
                        name="column-3-2-semantic", description="test", keywords=[],
                    ),
                    "statistical_properties": RColumnStatisticsAspect(
                        name="column-3-2-statistic",
                        non_null_count=0,
                        null_count=0,
                        numerical_stats=None,
                        categorical_stats=RCategoricalStatistics(
                            value_counts={"1": 1, "2": 2},
                        ),
                    ),
                    "schema_properties"     : RColumnSchemaAspect(
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
                link_id=uuid.uuid4(),
                name="table-1-column-1-1",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[3].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
                name="table-1-column-1-2",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[4].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
                name="table-2-column-2-1",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[5].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
                name="table-2-column-2-2",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[6].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
                name="table-3-column-3-1",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[7].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
                name="table-3-column-3-2",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[8].asset_id,
            ),
            Link(
                link_id=uuid.uuid4(),
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
                    ),
                },
            ),
            Link(
                link_id=uuid.uuid4(),
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
                    ),
                },
            ),
        ]
        self.graph = DatabaseGraph(assets, links)
        self.uri = "sqlite+aiosqlite:///:memory:"

    async def test_insert_and_delete_graph(self):
        target_id = uuid.uuid4()
        persistent = await async_persistent(self.uri)
        await persistent.insert_graph(target_id, "test")
        graph_name = await persistent.get_graph_name(target_id)
        self.assertEqual("test", graph_name)
        await persistent.delete_graph(target_id)
        with self.assertRaises(GraphNotFound):
            _ = await persistent.get_graph_name(target_id)

    async def test_crd_assets(self):
        target_id = uuid.uuid4()
        persistent = await async_persistent(self.uri)
        await persistent.insert_graph(target_id, "test")
        await persistent.insert_assets(self.graph.assets, target_id)
        assets = await persistent.get_assets(target_id)
        self.assertEqual(
            set(self.graph.assets),
            set(assets),
        )
        await persistent.delete_assets(
            [a.asset_id for a in self.graph.assets], target_id,
        )
        assets = await persistent.get_assets(target_id)
        self.assertEqual(0, len(assets))

    async def test_crd_links(self):
        target_id = uuid.uuid4()
        persistent = await async_persistent(self.uri)
        await persistent.insert_graph(target_id, "test")
        await persistent.insert_assets(self.graph.assets, target_id)
        await persistent.insert_links(self.graph.links, target_id)
        links = await persistent.get_links(target_id)
        self.assertEqual(
            set(self.graph.links),
            set(links),
        )
        await persistent.delete_links(
            [link.link_id for link in self.graph.links],
            target_id,
        )
        links = await persistent.get_links(target_id)
        self.assertEqual(0, len(links))

    async def test_crd_asset_aspect(self):
        target_id = uuid.uuid4()
        persistent = await async_persistent(self.uri)
        await persistent.insert_graph(target_id, "test")
        target_asset = self.graph.assets[0]
        await persistent.insert_assets([target_asset], target_id)
        await persistent.insert_asset_aspects(
            target_asset.aspects, target_asset.asset_id,
        )
        aspects = await persistent.get_asset_aspects(
            target_asset.asset_id, AssetType.RTABLE,
        )
        self.assertEqual(
            target_asset.aspects,
            aspects
        )

    async def test_crd_link_aspect(self):
        target_id = uuid.uuid4()
        persistent = await async_persistent(self.uri)
        await persistent.insert_graph(target_id, "test")
        source_asset = self.graph.assets[0]
        dest_asset = self.graph.assets[3]
        target_link = self.graph.links[0]
        await persistent.insert_assets([source_asset, dest_asset], target_id)
        await persistent.insert_links([target_link], target_id)
        await persistent.insert_link_aspects(target_link.aspects, target_link.link_id)
        aspects = await persistent.get_link_aspects(
            source_asset.asset_id, LinkType.CONTAIN,
        )
        self.assertEqual(
            target_link.aspects,
            aspects
        )


if __name__ == '__main__':
    unittest.main()
