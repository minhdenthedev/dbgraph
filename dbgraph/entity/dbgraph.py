from __future__ import annotations

import itertools
from dataclasses import dataclass

import rustworkx as rx

from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


@dataclass
class DatabaseGraph:
    """
    Represent the full graph of the database.
    """

    assets: list[Asset]
    links: list[Link]

    def __post_init__(self):
        self._nodes_idx = {a.asset_id: i for i, a in enumerate(self.assets)}
        self._nodes_data = {i: a for i, a in enumerate(self.assets)}
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

    def to_markdown(self) -> str:
        """Describe this graph using Markdown"""
        markdown = ""
        tables = [a for a in self._nodes_data.values() if a.type == AssetType.RTABLE]
        for table in tables:
            markdown += table.to_markdown() + "\n"
            columns = self.get_neighbors(table.asset_id, LinkType.CONTAIN)
            for column in columns:
                markdown += column.to_markdown() + "\n"
        fks = [
            link
            for link in self._edges_data.values()
            if link.type == LinkType.FOREIGN_KEY
        ]
        if len(fks) > 0:
            markdown += "## List of foreign keys constraints\n"
            for fk in fks:
                src_name = self._nodes_data[self._nodes_idx[fk.source_id]].name
                dst_name = self._nodes_data[self._nodes_idx[fk.destination_id]].name
                markdown += fk.to_markdown(src_name, dst_name)
        return markdown

    def get_neighbors_sub_graph(
        self, asset_id: str, link_type: LinkType
    ) -> DatabaseGraph:
        node_idx = self._nodes_idx[asset_id]
        links: dict[int, Link] = self._graph.adj(node_idx)
        target_links = [link for link in links.values() if link.type == link_type]
        assets_ids = {self._nodes_idx[link.destination_id] for link in target_links}
        assets_ids.update({self._nodes_idx[link.source_id] for link in target_links})
        assets = [self._nodes_data[i] for i in assets_ids]
        assets.append(self._nodes_data[node_idx])
        return DatabaseGraph(assets, target_links)

    def find_shortest_paths_sub_graphs(
        self, src_id: str, dst_id: str, visiting_ids: set[str]
    ) -> list[DatabaseGraph]:
        src_idx = self._nodes_idx[src_id]
        dst_idx = self._nodes_idx[dst_id]
        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        if len(visiting_ids) == 0:
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
        return [
            self._nodes_data[self._nodes_idx[link.destination_id]]
            for link in target_links
        ]

    def find_shortest_paths(
        self, src_id: str, dst_id: str, visiting_ids: set[str]
    ) -> list[list[Asset]]:
        src_idx = self._nodes_idx[src_id]
        dst_idx = self._nodes_idx[dst_id]
        paths = rx.all_shortest_paths(self._graph, src_idx, dst_idx)

        if len(visiting_ids) == 0:
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
