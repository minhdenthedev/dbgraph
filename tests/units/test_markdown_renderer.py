import unittest
from pathlib import Path

from dbgraph import Link, LinkType, Asset, AssetType, DatabaseGraph
from dbgraph.io.json_graph_loader import JSONGraphLoader
from dbgraph.render.markdown_renderer import MarkdownRenderer


class TestMarkdownRenderer(unittest.TestCase):
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
        self.renderer = MarkdownRenderer()

    def test_render(self):
        markdown = self.renderer.render(self.dbgraph)
        self.assertIsInstance(markdown, str)


if __name__ == "__main__":
    unittest.main()
