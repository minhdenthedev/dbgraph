from abc import ABC, abstractmethod

from dbgraph.entity.dbgraph import DatabaseGraph


class GraphLoader(ABC):
    """Interface for classes that read graphs from disk"""

    @abstractmethod
    def load(self) -> DatabaseGraph:
        pass
