from abc import ABC, abstractmethod

from dbgraph.entity.rdbgraph import RDatabaseGraph


class GraphDescriptor(ABC):
    """Interface for class that generate semantic aspects for a database graph or a sub-graph"""

    @abstractmethod
    def rfill_semantic_aspects(self, graph: RDatabaseGraph) -> RDatabaseGraph:
        pass
