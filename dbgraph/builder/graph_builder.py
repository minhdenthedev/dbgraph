from abc import ABC, abstractmethod

from dbgraph.entity.asset import Asset
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link


class GraphBuilder(ABC):
    """Interface for relational database graph builder"""

    @abstractmethod
    def _build_assets(self) -> list[Asset]:
        pass

    @abstractmethod
    def _build_links(self) -> list[Link]:
        pass

    def build_graph(self) -> DatabaseGraph:
        assets = self._build_assets()
        links = self._build_links()
        return DatabaseGraph(assets, links)
