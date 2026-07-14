from abc import ABC, abstractmethod

from dbgraph.entity.aspect import SemanticAspect


class SearchEngine(ABC):
    """Interface for search engines"""

    @abstractmethod
    def search(self, text: str, top_k: int = 10) -> list[str]:
        """Search relevant resources and return list of IDs"""
        pass

    @abstractmethod
    def index(self, semantic_aspects: dict[str, SemanticAspect]):
        pass
