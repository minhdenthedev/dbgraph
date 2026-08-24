from abc import ABC, abstractmethod

from dbgraph.render.graph_renderer import GraphRenderer


class TextRenderer(GraphRenderer, ABC):
    """Render the graph to text-based representation"""

    @abstractmethod
    def get_content(self) -> str:
        """Get the text data"""
