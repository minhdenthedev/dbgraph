from argparse import ArgumentParser
from pathlib import Path

from dbgraph.application import Application
from dbgraph.io.json_graph_writer import JSONGraphWriter


class CLI:
    """Controlling the application's CLI"""

    def __init__(self, application: Application):
        self.application = application
        self.parser = ArgumentParser()
        subparsers = self.parser.add_subparsers(dest="command")

        config_parser = subparsers.add_parser(
            "config", help="Config DBGraph"
        )
        config_parser.add_argument(
            "--metadata_uri", "-mu", help="Set database URI to saved DBGraph's results"
        )

        run_parser = subparsers.add_parser(
            "run", help="Run DBGraph with source database URI"
        )
        run_parser.add_argument(
            "source_uri",
            help="The source database URI to run profiling and auto-documentation on",
        )
        run_parser.add_argument(
            "name",
            help="Name of the output graph"
        )
        run_parser.add_argument(
            "--json",
            "-js",
            metavar="JSON_PATH",
            help="If specified, the graph will also be saved to local machine in JSON format at given path",
        )
        run_parser.add_argument(
            "--describe",
            action='store_true',
            help="Whether or not to use LLM to describe the data assets",
            default=True
        )

        graph_parser = subparsers.add_parser(
            "graph", help="Manage graphs"
        )
        graph_parser.add_argument(
            "--list", "-ls", help="List graphs", action="store_true"
        )
        graph_parser.add_argument(
            "--remove", "-rm", help="Remove graph by ID", metavar="GRAPH_ID"
        )
        graph_parser.add_argument(
            "--markdown", "-md", help="Convert a graph into Markdown", metavar="MARKDOWN_PATH"
        )
        graph_parser.add_argument(
            "--json", "-js", help="Convert a graph to JSON", metavar="JSON_PATH"
        )

        _ = subparsers.add_parser(
            "server", help="Run DBGraph server and expose endpoints"
        )

    def process_run(self, source_uri: str, name: str, fill_semantic: bool, json_path: str | None):
        graph_id = self.application.build_graph(
            database_uri=source_uri, name=name, fill_semantic=fill_semantic,
        )
        print(f"Graph {name} built and stored! (ID={graph_id})")
        if json_path is not None:
            graph = self.application.load_graph(graph_id)
            writer = JSONGraphWriter(Path(json_path))
            writer.write(graph)
            print(f"Graph {name} is also saved in JSON format at: {json_path}")


    def run(self):
        args = self.parser.parse_args()
        match args.command:
            case "run":
                self.process_run(args.source_uri, args.name, args.describe, args.json_path)
            case _:
                raise RuntimeError(f"Command `{args.command}` doesn't exist!")
