from __future__ import annotations

from dbgraph import LinkType
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link


class RDatabaseGraph(DatabaseGraph):
    """Graph for Relational Database"""

    @staticmethod
    def from_graph(graph: DatabaseGraph) -> RDatabaseGraph:
        return RDatabaseGraph(graph.assets, graph.links)

    def get_columns(self, table_id: str) -> list[Asset]:
        """Get list of assets which are columns belong to this table

        Args:
            table_id: ID of the target table

        Returns:
            assets: columns belong to this table
        """
        neighbors = self.get_neighbors(table_id)
        return [n for n in neighbors if n.type == AssetType.RCOLUMN]

    def get_tables(self) -> list[Asset]:
        """Get all the tables in the graph"""
        return [a for a in self.assets if a.type == AssetType.RTABLE]

    def get_foreign_keys(self) -> list[Link]:
        """Get all foreign keys in the graph"""
        return [link for link in self.links if link.type == LinkType.FOREIGN_KEY]

    def get_connected_tables(self, table_id: str) -> list[Asset]:
        """Get all connected table

        Args:
            table_id: target table

        Returns:
            assets: list of references table
        """
        neighbors = self.get_neighbors(table_id)
        return [n for n in neighbors if n.type == AssetType.RTABLE]

    def select_connected_tables(self, table_id: str) -> RDatabaseGraph:
        """Get references tables with their columns

        Args:
            table_id: target table

        Returns:
            subgraph: the subgraph of which include connected tables and their columns
        """
        refs_tables = self.get_connected_tables(table_id)
        assets: list[Asset] = [table for table in refs_tables]
        target_table: Asset = self.get_asset(table_id)
        target_table_columns = self.get_columns(table_id)
        assets.append(target_table)
        assets.extend(target_table_columns)
        links: list[Link] = [
            self.get_link(target_table.asset_id, column.asset_id)
            for column in target_table_columns
        ]
        for table in refs_tables:
            fk_link = self.get_link(table_id, table.asset_id)
            links.append(fk_link)
            columns = self.get_columns(table.asset_id)
            for column in columns:
                assets.append(column)
                link = self.get_link(table.asset_id, column.asset_id)
                links.append(link)
        return RDatabaseGraph(assets, links)
