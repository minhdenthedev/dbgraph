from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from dbgraph.entity.aspect import SemanticAspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.rdbgraph import RDatabaseGraph


@dataclass
class GraphDescriptor(ABC):
    """Base class that generate semantic aspects for a database graph or a sub-graph"""

    max_workers: int

    @abstractmethod
    def get_semantic_aspect(self, asset: Asset, context: RDatabaseGraph) -> SemanticAspect:
        """Get the description of this asset.

        Args:
            asset: Target asset
            context: an instance of `RDatabaseGraph`, could be the whole database graph or a sub-graph

        Returns:
            semantic aspect for this asset
        """

    def rfill_semantic_aspects(self, graph: RDatabaseGraph) -> RDatabaseGraph:
        print("Building context...")
        tables = graph.get_tables()
        assets = tables
        contexts = [graph.select_connected_tables(table.asset_id) for table in tables]
        for table in tables:
            context = RDatabaseGraph(assets=[table], links=[])
            columns = graph.get_columns(table.asset_id)
            for column in columns:
                assets.append(column)
                contexts.append(context)
        print("Done building context")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = {
                asset.asset_id: future
                for asset, future in zip(
                    assets,
                    executor.map(self.get_semantic_aspect, assets, contexts)
                )
            }
        for key, aspect in results.items():
            asset = graph.get_asset(key)
            asset.aspects["semantic_properties"] = aspect
        return graph

    def rfill_semantic_aspects_seq(self, graph: RDatabaseGraph) -> RDatabaseGraph:
        print("Building context...")
        tables = graph.get_tables()
        assets = tables
        contexts = [graph.select_connected_tables(table.asset_id) for table in tables]
        for table in tables:
            context = RDatabaseGraph(assets=[table], links=[])
            columns = graph.get_columns(table.asset_id)
            for column in columns:
                assets.append(column)
                contexts.append(context)
        print("Done building context")
        results = {}
        for asset, context in zip(assets, contexts):
            results[asset.asset_id] = self.get_semantic_aspect(asset, context)
        for key, aspect in results.items():
            asset = graph.get_asset(key)
            asset.aspects["semantic_properties"] = aspect
        return graph
