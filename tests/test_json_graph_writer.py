import unittest
from pathlib import Path

from dbgraph.builder.sqlalchemy.sql_graph_builder import SQLAlchemyGraphBuilder
from dbgraph.io.json_graph_writer import JSONGraphWriter


class TestJSONGraphWriter(unittest.TestCase):
    def setUp(self):
        graph_builder = SQLAlchemyGraphBuilder("sqlite:///data/northwind.db")
        self.graph = graph_builder.build_graph()
        self.graph_writer = JSONGraphWriter(
            json_path=Path("data/northwind-graph-v4.json"), indent=2
        )

    def test_write(self):
        self.graph_writer.write(self.graph)


if __name__ == "__main__":
    unittest.main()
