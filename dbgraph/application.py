from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from dbgraph.builder.graph_builder import GraphBuilder
from dbgraph.builder.sql_graph_builder import SQLGraphBuilder
from dbgraph.descriptor.graph_descriptor import GraphDescriptor
from dbgraph.entity.asset import Asset
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.io.json_graph_loader import JSONGraphLoader
from dbgraph.io.json_graph_writer import JSONGraphWriter
from dbgraph.persistent.graph_persistent import GraphPersistent
from dbgraph.persistent.sql_graph_persistent import SQLGraphPersistent


@dataclass
class Application:
    """God class to control the logical flow within dbgraph"""

    source_database_type: str
    graph_persistent_uri: str
    graph_persistent_type: str
    descriptor: GraphDescriptor | None = None

    def __post_init__(self):
        self.graph_persistent = self.create_graph_persistent()

    def create_graph_builder(self, database_uri: str) -> GraphBuilder:
        match self.source_database_type:
            case "sql":
                builder = SQLGraphBuilder(database_uri)
            case _:
                raise NotImplementedError()
        return builder

    def create_graph_persistent(self) -> GraphPersistent:
        match self.graph_persistent_type:
            case "sql":
                persistent = SQLGraphPersistent(self.graph_persistent_uri)
            case _:
                raise NotImplementedError()
        return persistent

    def build_graph(self, name: str, database_uri: str, fill_semantic: bool) -> str:
        """Build the graph, return its ID in the database"""
        builder = self.create_graph_builder(database_uri)
        graph = builder.build_graph()
        if fill_semantic and self.descriptor is not None:
            graph = self.descriptor.rfill_semantic_aspects(
                RDatabaseGraph.from_graph(graph)
            )
        graph_id = str(uuid4())
        self.graph_persistent.create_graph(graph_id, name)
        self.graph_persistent.save_graph(graph, name)
        return graph_id

    def load_graph(self, graph_id: str) -> DatabaseGraph:
        """Load the graph using its ID"""
        return self.graph_persistent.load_graph(graph_id)

    def delete_graph(self, graph_id: str):
        """Delete the graph using its ID"""
        self.graph_persistent.delete_graph(graph_id)

    def get_asset(self, asset_id: str, graph_id: str) -> Asset:
        """Find an asset using its ID"""
        return self.graph_persistent.get_asset(asset_id, graph_id)

    def get_link(self, link_id: str, graph_id: str) -> Link:
        """Find a link using its ID"""
        return self.graph_persistent.get_link(link_id, graph_id)

    def write_to_json(self, graph_id: str, path: str):
        graph = self.graph_persistent.load_graph(graph_id)
        writer = JSONGraphWriter(Path(path))
        writer.write(graph)

    def load_from_json(self, path: str) -> DatabaseGraph:
        reader = JSONGraphLoader(Path(path))
        return reader.load()
