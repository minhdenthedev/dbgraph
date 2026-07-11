import unittest

from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


class TestDBGraph(unittest.TestCase):
    def setUp(self):
        assets = [
            Asset(asset_id="hello1", name="hello1", type=AssetType.RTABLE),
            Asset(asset_id="hello2", name="hello2", type=AssetType.RTABLE),
            Asset(asset_id="hello3", name="hello3", type=AssetType.RTABLE),
        ]
        links = [
            Link(
                link_id="1",
                name="12",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[0].asset_id,
                destination_id=assets[1].asset_id,
            ),
            Link(
                link_id="1",
                name="12",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[1].asset_id,
                destination_id=assets[2].asset_id,
            ),
        ]
        self.dbgraph = DatabaseGraph(assets, links)

    def test_shortest_paths(self):
        assets = self.dbgraph.find_shortest_paths("hello1", "hello3", set())
        print(assets)


if __name__ == "__main__":
    unittest.main()
