from __future__ import annotations

import itertools
from dataclasses import dataclass

import rustworkx as rx

from dbgraph.entity.asset import Asset
from dbgraph.entity.link import Link


@dataclass
class DatabaseGraph:
    """Represents a database as a graph of assets and relationships.

    A `DatabaseGraph` models the structure of a database using
    assets as nodes and links as relationships between those assets.
    It provides methods for creating, querying, and traversing the
    database structure in a graph-oriented way.

    Attributes:
        assets: The collection of `Asset` objects in the graph.
        links: The collection of `Link` objects representing
            relationships between assets.
    """

    assets: list[Asset]
    links: list[Link]

    def __post_init__(self):
        self._asset_id_to_node_idx = {a.asset_id: i for i, a in enumerate(self.assets)}
        self._nodes_data = {i: asset for i, asset in enumerate(self.assets)}
        self._edges_data = {i: link for i, link in enumerate(self.links)}
        links_tuples = [
            (
                self._asset_id_to_node_idx[link.source_id],
                self._asset_id_to_node_idx[link.destination_id],
                link,
            )
            for link in self.links
        ]
        self._graph = rx.PyGraph()
        self._graph.add_nodes_from(self.assets)
        self._graph.add_edges_from(links_tuples)

    def _node_idx(self, asset_id: str) -> int:
        try:
            return self._asset_id_to_node_idx[asset_id]
        except KeyError:
            raise KeyError(f"Asset with id={asset_id} not found!")

    def _neighbors(self, asset_id: str) -> tuple[set[int], list[Link]]:
        """Return list of asset's indices in the graph and those links"""
        node_idx = self._node_idx(asset_id)

        # Find links
        links: dict[int, Link] = self._graph.adj(node_idx)

        # Find assets indices
        asset_indices = {self._node_idx(link.destination_id) for link in links.values()}
        asset_indices = asset_indices.union({
            self._node_idx(link.source_id) for link in links.values()
        })

        return asset_indices, list(links.values())


    def get_asset(self, asset_id: str) -> Asset:
        """Return the asset using asset_id"""
        return self._graph.get_node_data(self._node_idx(asset_id))

    def get_link(self, src_id: str, dst_id: str) -> Link:
        """Return the link connect these two Assets"""
        return self._graph.get_edge_data(
            self._node_idx(src_id), self._node_idx(dst_id)
        )


    def select_neighbors(
        self, asset_id: str
    ) -> DatabaseGraph:
        """Get this node and its neighbors.

        Args:
            asset_id: ID of the asset to be queried

        Return:
            subgraph: an instance of `DatabaseGraph` as subgraph
        """

        asset_indices, links = self._neighbors(asset_id)
        assets = [self._graph.get_node_data(i) for i in asset_indices]
        return DatabaseGraph(assets, links)

    def select_shortest_paths(
        self, src_id: str, dst_id: str
    ) -> list[DatabaseGraph]:
        """
        Find shortest paths between two Assets.

        Args:
            src_id: ID of the source asset
            dst_id: ID of the destination asset

        Returns:
            subgraphs: list of `DatabaseGraph` which are the shortest paths
                between source and destination Assets
        """
        src_idx = self._node_idx(src_id)
        dst_idx = self._node_idx(dst_id)

        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        # Get a list of lists of assets
        assets_lists = [[self._graph.get_node_data(i) for i in path] for path in paths]

        # Get a list of lists of links
        pairs_lists = [itertools.pairwise(path) for path in paths]
        links_lists = [
            [self._graph.get_edge_data(pair[0], pair[1]) for pair in pairs]
            for pairs in pairs_lists
        ]
        return [
            DatabaseGraph(assets, links)
            for assets, links in zip(assets_lists, links_lists)
        ]

    def get_neighbors(self, asset_id: str) -> list[Asset]:
        """Get neighbors assets of an asset

        Args:
            asset_id: target asset

        Return:
            list of neighbor `Asset`s
        """
        asset_indices, _ = self._neighbors(asset_id)
        # Remove itself
        try:
            asset_indices.remove(self._node_idx(asset_id))
        except KeyError:
            pass
        return [self._graph.get_node_data(i) for i in asset_indices]

    def find_shortest_paths(
        self, src_id: str, dst_id: str
    ) -> list[list[Asset]]:
        """Find shortest paths between two Assets

        Args:
            src_id: ID of the source asset
            dst_id: ID of the destination asset

        Returns:
            assets: list of lists of assets. Each list is a shortest path
                from source Asset to destination Asset
        """
        src_idx = self._node_idx(src_id)
        dst_idx = self._node_idx(dst_id)
        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        return [[self._graph.get_node_data(i) for i in path] for path in paths]
