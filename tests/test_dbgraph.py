import unittest

from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


class TestDBGraph(unittest.TestCase):
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
        self.dbgraph = DatabaseGraph(assets, links)

    def test_select_neighbors(self):
        # table-1 -> [table-2, column-1-1, column-1-2]
        subgraph = self.dbgraph.select_neighbors("1")
        subgraph.assets.sort(key=lambda x: x.asset_id)
        subgraph.links.sort(key=lambda x: x.link_id)
        self.assertIsInstance(subgraph, DatabaseGraph)
        self.assertEqual(len(subgraph.assets), 4)
        self.assertEqual(len(subgraph.links), 3)
        self.assertEqual([asset.asset_id for asset in subgraph.assets], ["1", "2", "4", "5"])
        self.assertEqual([link.link_id for link in subgraph.links], ["1", "2", "7"])

        # column-1-1 -> [table-1]
        subgraph = self.dbgraph.select_neighbors("4")
        self.assertEqual(len(subgraph.assets), 2)
        self.assertEqual([asset.asset_id for asset in subgraph.assets], ["1", "4"])

    def test_get_neighbors(self):
        # table-1 -> [table-2, column-1-1, column-1-2]
        assets = self.dbgraph.get_neighbors("1")
        self.assertEqual(len(assets), 3)
        self.assertEqual([asset.asset_id for asset in assets], ["2", "4", "5"])

        # column-1-1 -> [table-1]
        assets = self.dbgraph.get_neighbors("4")
        self.assertEqual(len(assets), 1)
        self.assertEqual([asset.asset_id for asset in assets], ["1"])

    def test_select_shortest_paths(self):
        # column-1-1 -> table-1 -> table-2 -> table-3 -> column-3-2
        subgraphs = self.dbgraph.select_shortest_paths("4", "9")
        self.assertEqual(len(subgraphs), 1)
        subgraph = subgraphs[0]
        self.assertEqual(len(subgraph.assets), 5)
        self.assertEqual(len(subgraph.links), 4)
        self.assertEqual([asset.asset_id for asset in subgraph.assets], ["4", "1", "2", "3", "9"])
        self.assertEqual([link.link_id for link in subgraph.links], ["1", "7", "8", "6"])

    def test_find_shortest_paths(self):
        # column-1-1 -> table-1 -> table-2 -> table-3 -> column-3-2
        assets = self.dbgraph.find_shortest_paths("4", "9")[0]
        self.assertEqual(len(assets), 5)
        self.assertEqual([asset.asset_id for asset in assets], ["4", "1", "2", "3", "9"])


if __name__ == "__main__":
    unittest.main()
