from dataclasses import dataclass
from pathlib import Path

import bm25s
import Stemmer

from dbgraph.entity.aspect import SemanticAspect
from dbgraph.search.search_engine import SearchEngine


@dataclass
class BM25SearchEngine(SearchEngine):
    """Implementation of SearchEngine using BM25"""

    index_path: Path

    def search(self, text: str, top_k: int = 10) -> list[str]:
        retriever = bm25s.BM25.load(self.index_path, load_corpus=True)
        stemmer = Stemmer.Stemmer("english")
        tokens = bm25s.tokenize(text, stopwords="en", stemmer=stemmer)
        results, _ = retriever.retrieve(tokens, k=top_k)
        results = results[0]
        return [r["id"] for r in results]

    def index(self, semantic_aspects: dict[str, SemanticAspect]):
        stemmer = Stemmer.Stemmer("english")
        corpus = [{"id": k, "text": v.description} for k, v in semantic_aspects.items()]
        tokens = bm25s.tokenize(
            [doc["text"] for doc in corpus], stopwords="en", stemmer=stemmer
        )
        retriever = bm25s.BM25(corpus=corpus)
        retriever.index(tokens)
        retriever.save(self.index_path)
