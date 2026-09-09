from abc import ABC, abstractmethod

from dbgraph.entity.dbgraph import DatabaseGraph


class GraphRenderer(ABC):
    """Interface for rendering the graph"""

    @abstractmethod
    def render(self, graph: DatabaseGraph) -> str:
        """Render the graph to text-based format"""
