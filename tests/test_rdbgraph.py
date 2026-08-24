import unittest
from pathlib import Path

from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.io.json_graph_loader import JSONGraphLoader


class TestRDatabaseGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_loader = JSONGraphLoader(Path("data/northwind-graph.json"))
        dbgraph = self.graph_loader.load()
        self.graph = RDatabaseGraph(
            list(dbgraph._nodes_data.values()), list(dbgraph._edges_data.values())
        )

    def test_get_refs_with_columns(self):
        subgraph = self.graph.get_refs_with_columns(
            "20414a87-96a2-4314-887c-a247daf4b160"
        )
        print(subgraph.to_markdown())


if __name__ == "__main__":
    unittest.main()
