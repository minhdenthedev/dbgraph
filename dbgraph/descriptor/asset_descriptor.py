from abc import ABC, abstractmethod

from dbgraph.entity.dbgraph import DatabaseGraph


class AssetDescriptor(ABC):
    """Interface for class that generate semantic aspects for a database graph"""

    @abstractmethod
    def fill_semantic_aspects(self, graph: DatabaseGraph) -> DatabaseGraph:
        pass
