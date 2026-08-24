import unittest
from pathlib import Path

from dbgraph.io.json_graph_loader import JSONGraphLoader
from dbgraph.render.markdown_renderer import MarkdownRenderer


class TestMarkdownRenderer(unittest.TestCase):
    def setUp(self):
        graph_loader = JSONGraphLoader(Path("data/northwind-graph-v2.json"))
        self.graph = graph_loader.load()
        self.renderer = MarkdownRenderer()

    def test_render(self):
        self.renderer.render(self.graph)
        self.assertIsInstance(self.renderer.get_content(), str)


if __name__ == "__main__":
    unittest.main()
