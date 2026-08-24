import unittest

from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType
from dbgraph.entity.rdbgraph import RDatabaseGraph


class TestRDBGraph(unittest.TestCase):
    def setUp(self):
        assets = [
            Asset(asset_id="1", name="table-1", type=AssetType.RTABLE),
            Asset(asset_id="2", name="table-2", type=AssetType.RTABLE),
            Asset(asset_id="3", name="table-3", type=AssetType.RTABLE),
            Asset(asset_id="4", name="column-1-1", type=AssetType.RCOLUMN),
            Asset(asset_id="5", name="column-1-2", type=AssetType.RCOLUMN),
            Asset(asset_id="6", name="column-2-1", type=AssetType.RCOLUMN),
            Asset(asset_id="7", name="column-2-2", type=AssetType.RCOLUMN),
            Asset(asset_id="8", name="column-3-1", type=AssetType.RCOLUMN),
            Asset(asset_id="9", name="column-3-2", type=AssetType.RCOLUMN),
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
            ),
            Link(
                link_id="8",
                name="table-2-table-3",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[1].asset_id,
                destination_id=assets[2].asset_id,
            ),
        ]
        self.graph = RDatabaseGraph.from_graph(DatabaseGraph(assets, links))

    def test_get_columns(self):
        # table-1 -> [column-1-1, column-1-2]
        columns = self.graph.get_columns("1")
        columns.sort(key=lambda x: x.asset_id)
        self.assertEqual(len(columns), 2)
        self.assertEqual([col.asset_id for col in columns], ["4", "5"])

    def test_get_connected_tables(self):
        # table-1 -> **table-2** -> table-3
        tables = self.graph.get_connected_tables("2")
        tables.sort(key=lambda x: x.asset_id)
        self.assertEqual(len(tables), 2)
        self.assertEqual([table.asset_id for table in tables], ["1", "3"])

    def test_get_connected_tables_with_cols(self):
        # [column-1-1, column-1-2] - table-1 -- **table-2** -- table-3 - [column-3-1, column-3-2]
        subgraph = self.graph.select_connected_tables("2")
        self.assertEqual(len(subgraph.assets), 9)
        self.assertEqual(len(subgraph.links), 8)

        subgraph = self.graph.select_connected_tables("1")
        self.assertEqual(len(subgraph.assets), 6)
        self.assertEqual(len(subgraph.links), 5)
        subgraph.assets.sort(key=lambda x: x.asset_id)
        subgraph.links.sort(key=lambda x: x.link_id)
        self.assertEqual([a.asset_id for a in subgraph.assets], ["1", "2", "4", "5", "6", "7"])
        self.assertEqual([link.link_id for link in subgraph.links], ["1", "2", "3", "4", "7"])



if __name__ == "__main__":
    unittest.main()
