from abc import ABC, abstractmethod

from dbgraph.entity.dbgraph import DatabaseGraph


class GraphWriter(ABC):
    """Interface for classes that write graph to disk"""

    @abstractmethod
    def write(self, graph: DatabaseGraph):
        pass
