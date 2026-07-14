import unittest
from pathlib import Path

from dbgraph.descriptor.graph_descriptor_v1 import GraphDescriptorV1
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.io.json_graph_loader import JSONGraphLoader
from dbgraph.io.json_graph_writer import JSONGraphWriter
from dbgraph.llm.oai_llm import OAICompatibleLLM


class TestGraphDescriptorV1(unittest.TestCase):
    def setUp(self) -> None:
        formatting_prompt = """
# OUTPUT & FORMATTING
Return a JSON output with following schema: {`table or column's name`: {\"description\": ..., \"keywords\": [...]}}. Here are some guildlines you MUST follow when outputing your response:
- DO NOT add any comments nor explanations, return plain JSON output as I stated above.
- The description should be short and concise, only describe what information the table or column holds and what is the use of the table. DO NOT add example values in the description.
- The keywords should be short and relevant to the topic or the nature of the table or column.
- The descriptions and keywords should be easy to search for when using search engines like Google, ElasticSearch, ...
        """
        self.graph_descriptor = GraphDescriptorV1(
            llm=OAICompatibleLLM(
                model="ic_coding_assistant",
                base_url="https://code-assistant.icenter.ai/v1",
                api_key="vnpt1235",
            ),
            system_prompt="# ROLES & OBJECTIVES\nYou are an expert database analyst. Your task is to generate descriptions and keywords for tables and columns.This is the schema relevant to the user's task:",
            formating_prompt=formatting_prompt,
            target_prompt="# TASK DETAILS\nGenerate descriptions and keywords for {asset_type} `{asset_name}` and its columns:\n{columns_str}\nRemember use to the UUIDs I gave you. DO NOT generate fake UUIDs.",
        )
        graph = JSONGraphLoader(Path("data/northwind-graph.json")).load()
        self.graph = RDatabaseGraph(
            list(graph._nodes_data.values()), list(graph._edges_data.values())
        )

    def test_rfill_semantic_aspects(self):
        graph = self.graph_descriptor.rfill_semantic_aspects(self.graph)
        graph_writer = JSONGraphWriter(Path("data/northwind-graph-v2.json"), indent=2)
        graph_writer.write(graph)


if __name__ == "__main__":
    unittest.main()
