from abc import ABC, abstractmethod

from dbgraph.entity.aspect import Aspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link


class GraphPersistent(ABC):
    """Interface for graph persistent component, which save and load the graphs"""

    @abstractmethod
    def create_graph(self, graph_id: str, graph_name: str):
        """Insert the graph in the database"""

    @abstractmethod
    def delete_graph(self, graph_id: str):
        """Delete a graph and return it"""

    @abstractmethod
    def insert_assets(self, assets: list[Asset], graph_id: str):
        """Insert the assets into database"""

    @abstractmethod
    def insert_asset(self, asset: Asset, graph_id: str):
        """Insert a single asset"""

    @abstractmethod
    def insert_links(self, links: list[Link], graph_id: str):
        """Insert links into database"""

    @abstractmethod
    def insert_link(self, link: Link, graph_id: str):
        """Insert a single link into the database"""

    @abstractmethod
    def remove_assets(self, assets_ids: list[str], graph_id: str):
        """Remove the assets from the database"""

    @abstractmethod
    def remove_asset(self, asset_id: str, graph_id: str):
        """Remove the asset from the database"""

    @abstractmethod
    def remove_links(self, links_ids: list[str], graph_id: str):
        """Remove the links"""

    @abstractmethod
    def remove_link(self, link_id: str, graph_id: str):
        """Remove the link"""

    @abstractmethod
    def insert_asset_aspects(self, asset_id: str, aspects: dict[str, Aspect]):
        """Insert aspects into asset"""

    @abstractmethod
    def get_asset(self, asset_id: str, graph_id: str) -> Asset:
        """Find asset by its ID"""

    @abstractmethod
    def get_link(self, link_id: str, graph_id: str) -> Link:
        """Find link by its ID"""

    @abstractmethod
    def insert_link_aspects(self, link_id: str, aspects: dict[str, Aspect]):
        """Insert aspects into link"""

    @abstractmethod
    def get_aspects_of_asset(self, asset_id: str) -> dict[str, Aspect]:
        """Get the aspects of an asset"""

    @abstractmethod
    def get_aspects_of_link(self, link_id: str) -> dict[str, Aspect]:
        """Get the aspects of a link"""

    @abstractmethod
    def get_assets(self, graph_id: str) -> list[Asset]:
        """Return list of assets in a graph"""

    @abstractmethod
    def get_links(self, graph_id: str) -> list[Link]:
        """Return list of links in a graph"""

    @abstractmethod
    def load_graph(self, graph_id: str) -> DatabaseGraph:
        """Load the full database graph"""

    @abstractmethod
    def save_graph(self, graph: DatabaseGraph, graph_id: str):
        """Save the graph into database"""

    @abstractmethod
    def set_graph_state(self, graph_id: str, completed: bool):
        """Mark the graph as completely built and saved in the database or hasn't been finished building yet"""

    @abstractmethod
    def get_graph_info(self, graph_id: str) -> tuple[str, str, bool]:
        """Return the graph's info, which is a tuple containing [graph_id, graph_name, completed]"""
