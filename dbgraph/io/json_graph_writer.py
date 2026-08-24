import json
from dataclasses import asdict, dataclass
from pathlib import Path

from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.io.graph_writer import GraphWriter


@dataclass
class JSONGraphWriter(GraphWriter):
    json_path: Path
    indent: int | None = None

    def write(self, graph: DatabaseGraph):
        graph_data = asdict(graph)
        with self.json_path.open("w") as f:
            json.dump(graph_data, f, indent=self.indent)
