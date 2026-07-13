from abc import ABC, abstractmethod

from dbgraph.entity.asset import Asset
from dbgraph.entity.link import Link


class SearchEngine(ABC):
    """Interface for search engines"""

    @abstractmethod
    def search_assets(self, text: str) -> list[Asset]:
        pass

    @abstractmethod
    def search_links(self, text: str) -> list[Link]:
        pass
