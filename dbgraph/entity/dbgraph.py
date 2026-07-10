from dataclasses import dataclass

import rustworkx as rx

from dbgraph.entity.asset import Asset
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
                self._nodes_idx[link.source.asset_id],
                self._nodes_idx[link.destination.asset_id],
                link,
            )
            for link in self.links
        ]
        self._graph = rx.PyDiGraph()
        self._graph.add_nodes_from(self.assets)
        self._graph.add_edges_from(links_tuples)

    def get_neighbors(self, asset_id: str, link_type: LinkType) -> list[Asset]:
        node_idx = self._nodes_idx[asset_id]
        links: dict[int, Link] = self._graph.adj(node_idx)
        target_links = [link for link in links.values() if link.type == link_type]
        return [link.destination for link in target_links]

    def find_shortest_paths(
        self, src_id: str, dst_id: str, visiting_ids: set[str]
    ) -> list[list[Asset]]:
        src_idx = self._nodes_idx[src_id]
        dst_idx = self._nodes_idx[dst_id]
        paths = rx.digraph_all_shortest_paths(self._graph, src_idx, dst_idx)

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
