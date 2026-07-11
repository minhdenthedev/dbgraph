import unittest
from pathlib import Path

from dbgraph.io.json_graph_loader import JSONGraphLoader


class TestJSONGraphLoader(unittest.TestCase):
    def setUp(self):
        self.graph_loader = JSONGraphLoader(json_path=Path("data/northwind-graph.json"))

    def test_write(self):
        graph = self.graph_loader.load()
        print(graph)


if __name__ == "__main__":
    unittest.main()
