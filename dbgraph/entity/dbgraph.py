from __future__ import annotations

import itertools
from dataclasses import dataclass

import rustworkx as rx

from dbgraph.entity.asset import Asset
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


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
        self._nodes_idx = {a.asset_id: i for i, a in enumerate(self.assets)}
        self._nodes_data = {i: asset for i, asset in enumerate(self.assets)}
        self._edges_data = {i: link for i, link in enumerate(self.links)}
        links_tuples = [
            (
                self._nodes_idx[link.source_id],
                self._nodes_idx[link.destination_id],
                link,
            )
            for link in self.links
        ]
        self._graph = rx.PyGraph()
        self._graph.add_nodes_from(self.assets)
        self._graph.add_edges_from(links_tuples)

    def get_neighbors_sub_graph(
        self, asset_id: str, link_type: LinkType
    ) -> DatabaseGraph:
        node_idx = self._nodes_idx[asset_id]
        links: dict[int, Link] = self._graph.adj(node_idx)
        target_links = [link for link in links.values() if link.type == link_type]
        assets_ids = {self._nodes_idx[link.destination_id] for link in target_links}
        if link_type == LinkType.FOREIGN_KEY:
            assets_ids.update(
                {self._nodes_idx[link.source_id] for link in target_links}
            )
        assets_ids.add(self._nodes_idx[asset_id])
        assets = [self._nodes_data[i] for i in assets_ids]
        return DatabaseGraph(assets, target_links)

    def find_shortest_paths_sub_graphs(
        self, src_id: str, dst_id: str, visiting_ids: set[str] | None = None
    ) -> list[DatabaseGraph]:
        src_idx = self._nodes_idx[src_id]
        dst_idx = self._nodes_idx[dst_id]
        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        if visiting_ids is None:
            assets_lists = [[self._nodes_data[i] for i in path] for path in paths]
            pairs_lists = [itertools.pairwise(path) for path in paths]
            links_lists = [
                [self._graph.get_edge_data(pair[0], pair[1]) for pair in pairs]
                for pairs in pairs_lists
            ]
            return [
                DatabaseGraph(assets, links)
                for assets, links in zip(assets_lists, links_lists)
            ]

        asset_id_lists = [
            [self._nodes_data[i].asset_id for i in path] for path in paths
        ]
        paths = [
            [self._nodes_idx[asset_id] for asset_id in asset_id_list]
            for asset_id_list in asset_id_lists
            if visiting_ids.issubset(asset_id_list)
        ]
        assets_lists = [[self._nodes_data[i] for i in path] for path in paths]
        pairs_lists = [itertools.pairwise(path) for path in paths]
        links_lists = [
            [self._graph.get_edge_data(pair[0], pair[1]) for pair in pairs]
            for pairs in pairs_lists
        ]
        return [
            DatabaseGraph(assets, links)
            for assets, links in zip(assets_lists, links_lists)
        ]

    def get_neighbors(self, asset_id: str, link_type: LinkType) -> list[Asset]:
        node_idx = self._nodes_idx[asset_id]
        links: dict[int, Link] = self._graph.adj(node_idx)
        target_links = [link for link in links.values() if link.type == link_type]
        assets_ids = {self._nodes_idx[link.destination_id] for link in target_links}
        if link_type == LinkType.FOREIGN_KEY:
            assets_ids.update(
                {self._nodes_idx[link.source_id] for link in target_links}
            )
            assets_ids.remove(self._nodes_idx[asset_id])
        assets = [self._nodes_data[i] for i in assets_ids]

        return assets

    def find_shortest_paths(
        self, src_id: str, dst_id: str, visiting_ids: set[str] | None = None
    ) -> list[list[Asset]]:
        src_idx = self._nodes_idx[src_id]
        dst_idx = self._nodes_idx[dst_id]
        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        if visiting_ids is None:
            return [[self._nodes_data[i] for i in path] for path in paths]

        asset_id_lists = [
            [self._nodes_data[i].asset_id for i in path] for path in paths
        ]
        suitable_paths = [
            [self._nodes_idx[asset_id] for asset_id in asset_id_list]
            for asset_id_list in asset_id_lists
            if visiting_ids.issubset(asset_id_list)
        ]

        return [[self._nodes_data[i] for i in path] for path in suitable_paths]
