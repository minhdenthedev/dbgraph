import unittest
from pathlib import Path

from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link_type import LinkType
from dbgraph.io.json_graph_loader import JSONGraphLoader


class TestJSONGraphLoader(unittest.TestCase):
    def setUp(self):
        self.graph_loader = JSONGraphLoader(json_path=Path("data/northwind-graph.json"))

    def test_load(self):
        graph = self.graph_loader.load()
        self.assertIsInstance(graph, DatabaseGraph)

    def test_find_shortest_paths_sub_graphs(self):
        graph = self.graph_loader.load()
        subgraphs = graph.find_shortest_paths_sub_graphs(
            "601fca0f-9c27-4833-86d0-48f8383437a0",
            "29fb86b7-13f6-4a23-ab24-26d68881624f",
            set(),
        )
        print(subgraphs[0].to_markdown())

    def test_get_neighbors_sub_graph(self):
        graph = self.graph_loader.load()
        subgraph = graph.get_neighbors_sub_graph(
            "8ab5a624-0596-497e-a0ee-3996d95dbe63", LinkType.CONTAIN
        )
        self.assertIsInstance(subgraph, DatabaseGraph)
        # print(subgraph.to_markdown())

    def test_get_neighbors_sub_graph_fk(self):
        graph = self.graph_loader.load()
        subgraph = graph.get_neighbors_sub_graph(
            "8ab5a624-0596-497e-a0ee-3996d95dbe63", LinkType.FOREIGN_KEY
        )
        # print(subgraph.to_markdown())


if __name__ == "__main__":
    unittest.main()
