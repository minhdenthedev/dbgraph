import unittest
from pathlib import Path
from typing import cast

from dbgraph.entity.aspect import SemanticAspect
from dbgraph.io.json_graph_loader import JSONGraphLoader
from dbgraph.search.bm25_search_engine import BM25SearchEngine


class TestBM25SearchEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.search_engine = BM25SearchEngine(Path("data/northwind-index"))

    def test_index(self):
        graph_loader = JSONGraphLoader(Path("data/northwind-graph-v2.json"))
        graph = graph_loader.load()
        semantic_aspects = {
            a.asset_id: cast(SemanticAspect, a.aspects["semantic_properties"])
            for a in graph.assets
        }
        self.search_engine.index(semantic_aspects)

    def test_search(self):
        ids = self.search_engine.search(
            "Give me the total count of orders in each categories"
        )
        print(ids)


if __name__ == "__main__":
    unittest.main()
