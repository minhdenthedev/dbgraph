from abc import ABC, abstractmethod
from uuid import UUID

from dbgraph import DatabaseGraph, Asset, Link, AssetType, LinkType
from dbgraph.entity.aspect import Aspect


class GraphPersistentV2(ABC):
    """Interface for new persistent layer"""

    @abstractmethod
    def insert_graph(self, graph_id: UUID, graph_name: str):
        """Insert an empty graph into database"""

    @abstractmethod
    def save_graph(self,
                   graph_id: UUID,
                   graph_name: str,
                   graph: DatabaseGraph):
        """Save the graph into database"""

    @abstractmethod
    def load_graph(self, graph_id: UUID) -> DatabaseGraph:
        """Load the graph from database"""

    @abstractmethod
    def get_graph_name(self, graph_id: UUID) -> str:
        """Return the graph's name"""

    @abstractmethod
    def delete_graph(self, graph_id: UUID):
        """Delete the graph from the database"""

    @abstractmethod
    def insert_assets(self, assets: list[Asset], graph_id: UUID):
        """Insert assets into a graph in database"""

    @abstractmethod
    def insert_links(self, links: list[Link], graph_id: UUID):
        """Insert links into a graph in database"""

    @abstractmethod
    def delete_assets(self, asset_ids: list[UUID], graph_id: UUID):
        """Remove assets from a graph"""

    @abstractmethod
    def delete_links(self, link_ids: list[UUID], graph_id: UUID):
        """Remove links from a graph"""

    @abstractmethod
    def get_links(self, graph_id: UUID) -> list[Link]:
        """Return links in a graph"""

    @abstractmethod
    def get_assets(self, graph_id: UUID) -> list[Asset]:
        """Return assets in a graph"""

    @abstractmethod
    def insert_asset_aspects(self,
                             aspects: dict[str, Aspect],
                             asset_id: UUID):
        """Insert aspects into asset"""

    @abstractmethod
    def insert_link_aspects(self,
                            aspects: dict[str, Aspect],
                            link_id: UUID):
        """Insert aspects into link"""

    @abstractmethod
    def get_asset_aspects(self, asset_id: UUID, asset_type: AssetType) -> dict[str, Aspect]:
        """Get the aspects of an asset"""

    @abstractmethod
    def get_link_aspects(self, link_id: UUID, link_type: LinkType) -> dict[str, Aspect]:
        """Get the aspects of a link"""
