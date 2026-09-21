import unittest
import uuid
from datetime import datetime

from dbgraph.entity.aspect import (
    RCategoricalStatistics,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RNumericalStatistics,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    SemanticAspect, RTemporalStatistics,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType
from dbgraph.persistent import graph_persistent
from dbgraph.persistent.orm_graph_persistent import ORMGraphPersistent


class TestORMGraphPersistent(unittest.TestCase):
    def setUp(self) -> None:
        assets = [
            Asset(
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                        numerical_stats=None,
                        categorical_stats=None,
                        temporal_stats=RTemporalStatistics(
                            min_time=datetime.now(),
                            max_time=datetime.now(),
                            mode_time=datetime.now(),
                            num_uniques=3
                        )
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                asset_id=uuid.uuid4(),
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
                    )
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
                    )
                },
            ),
        ]
        self.graph = DatabaseGraph(assets, links)
        self.persistent = ORMGraphPersistent("sqlite:///:memory:")

    def test_insert_graph(self):
        target_id = uuid.uuid4()
        target_name = "test-name"
        self.persistent.insert_graph(target_id, target_name)
        name = self.persistent.get_graph_name(target_id)
        self.assertEqual(target_name, name)

    def test_crud_assets(self):
        target_id = uuid.uuid4()
        self.persistent.insert_graph(target_id, "test")
        self.persistent.insert_assets(self.graph.assets, target_id)
        assets = self.persistent.get_assets(target_id)
        target_ids = set(a.asset_id for a in self.graph.assets)
        asset_ids = set(a.asset_id for a in assets)
        self.assertEqual(target_ids, asset_ids)
        self.persistent.delete_assets(list(asset_ids), target_id)
        assets = self.persistent.get_assets(target_id)
        self.assertEqual(0, len(assets))

    def test_crud_links(self):
        target_id = uuid.uuid4()
        self.persistent.insert_graph(target_id, "test")
        self.persistent.insert_links(self.graph.links, target_id)
        links = self.persistent.get_links(target_id)
        links.sort(key=lambda x: x.link_id)
        target_links = self.graph.links
        target_links.sort(key=lambda x: x.link_id)
        for target_link, link in zip(target_links, links):
            self.assertEqual(target_link.link_id, link.link_id)
            self.assertEqual(target_link.source_id, link.source_id)
            self.assertEqual(target_link.destination_id, link.destination_id)

        link_ids = [link.link_id for link in links]
        self.persistent.delete_links(link_ids, target_id)
        links = self.persistent.get_links(target_id)
        self.assertEqual(0, len(links))

    def test_cr_asset_aspect(self):
        graph_id = uuid.uuid4()
        self.persistent.insert_graph(graph_id, "test")
        self.persistent.insert_assets(self.graph.assets, graph_id)
        for asset in self.graph.assets:
            self.persistent.insert_asset_aspects(
                asset.aspects, asset.asset_id
            )
            aspects = self.persistent.get_asset_aspects(
                asset.asset_id,
                asset.type
            )
            self.assertEqual(set(asset.aspects), set(aspects))

    def test_cr_link_aspect(self):
        graph_id = uuid.uuid4()
        self.persistent.insert_graph(graph_id, "test")
        self.persistent.insert_links(self.graph.links, graph_id)
        for link in self.graph.links:
            self.persistent.insert_link_aspects(link.aspects, link.link_id)
            aspects = self.persistent.get_link_aspects(
                link.link_id,
                link.type
            )
            self.assertEqual(set(link.aspects), set(aspects))

    def test_save_load_graph(self):
        target_id = uuid.uuid4()
        self.persistent.save_graph(
            target_id,
            "test",
            self.graph
        )
        graph = self.persistent.load_graph(target_id)
        self.assertEqual(self.graph, graph)

if __name__ == '__main__':
    unittest.main()
