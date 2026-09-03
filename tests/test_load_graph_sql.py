import unittest

from dbgraph import SQLGraphPersistent, SQLGraphBuilder


class TestLoadGraphSQL(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_builder = SQLGraphBuilder("sqlite:///data/northwind.db")
        self.persistent = SQLGraphPersistent("sqlite:///:memory:")

    def test_load(self):
        target_graph_id = "test-graph"
        target_graph = self.graph_builder.build_graph()
        self.persistent.save_graph(target_graph, target_graph_id)
        graph = self.persistent.load_graph(target_graph_id)
        self.assertEqual(len(target_graph.assets), len(graph.assets))
        self.assertEqual(len(target_graph.links), len(graph.links))


if __name__ == '__main__':
    unittest.main()
