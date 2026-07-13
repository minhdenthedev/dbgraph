from __future__ import annotations

from rustworkx.rustworkx import NoEdgeBetweenNodes

from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType


class RDatabaseGraph(DatabaseGraph):
    """Graph for Relational Database"""

    def get_columns(self, table_id: str) -> list[Asset]:
        return self.get_neighbors(table_id, LinkType.CONTAIN)

    def get_tables(self) -> list[Asset]:
        return [a for a in self._nodes_data.values() if a.type == AssetType.RTABLE]

    def get_references_tables(self, table_id: str) -> list[Asset]:
        return self.get_neighbors(table_id, LinkType.FOREIGN_KEY)

    def get_refs_with_columns(self, table_id: str) -> RDatabaseGraph:
        """Get references tables with their columns"""
        refs_tables = self.get_references_tables(table_id)
        assets: list[Asset] = [table for table in refs_tables]
        target_table = self._nodes_data[self._nodes_idx[table_id]]
        target_table_columns = self.get_columns(table_id)
        assets.append(target_table)
        assets.extend(target_table_columns)
        links: list[Link] = [
            self._graph.get_edge_data(
                self._nodes_idx[target_table.asset_id], self._nodes_idx[column.asset_id]
            )
            for column in target_table_columns
        ]
        for table in refs_tables:
            try:
                fk_link = self._graph.get_edge_data(
                    self._nodes_idx[table_id], self._nodes_idx[table.asset_id]
                )
            except NoEdgeBetweenNodes as e:
                print(self._nodes_idx[table_id], self._nodes_idx[table.asset_id])
                raise e
            links.append(fk_link)
            columns = self.get_columns(table.asset_id)
            for column in columns:
                assets.append(column)
                link = self._graph.get_edge_data(
                    self._nodes_idx[table.asset_id], self._nodes_idx[column.asset_id]
                )
                links.append(link)
        return RDatabaseGraph(assets, links)
