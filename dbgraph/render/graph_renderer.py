from abc import ABC, abstractmethod

from dbgraph.entity.dbgraph import DatabaseGraph


class GraphRenderer(ABC):
    """Interface for rendering the graph"""

    @abstractmethod
    def render(self, graph: DatabaseGraph):
        """Render the graph, store data inside the class"""
