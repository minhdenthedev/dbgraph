import os
import unittest
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from dbgraph.descriptor.prompt_templates import (
    COLUMN_QUESTION_PROMPT,
    COLUMN_SYSTEM_PROMPT,
    TABLE_QUESTION_PROMPT,
    TABLE_SYSTEM_PROMPT,
)
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.io.json_graph_writer import JSONGraphWriter
from dbgraph.render.markdown_renderer import MarkdownRenderer

load_dotenv()

from dbgraph.descriptor.langchain_graph_descriptor import LangchainGraphDescriptor
from dbgraph.io.json_graph_loader import JSONGraphLoader


class TestJSONGraphLoader(unittest.TestCase):
    def setUp(self):
        self.dbgraph = JSONGraphLoader(Path("data/northwind-graph.json")).load()
        model = ChatOpenAI(
            base_url=os.getenv("LLM_BASE_URL"),
            model=os.getenv("LLM_MODEL", ""),
            api_key=SecretStr(os.getenv("API_KEY", "")),
            extra_body={
                "extra_body": {"chat_template_kwargs": {"enable_thinking": False}}
            },
        )
        self.descriptor = LangchainGraphDescriptor(
            model=model,
            table_system_prompt=TABLE_SYSTEM_PROMPT,
            table_question_prompt=TABLE_QUESTION_PROMPT,
            column_system_prompt=COLUMN_SYSTEM_PROMPT,
            column_question_prompt=COLUMN_QUESTION_PROMPT,
            max_workers=4,
            markdown_renderer=MarkdownRenderer(),
        )

    def test_rfill(self):
        import time

        start = time.perf_counter()
        graph = self.descriptor.rfill_semantic_aspects(
            RDatabaseGraph.from_graph(self.dbgraph)
        )
        end = time.perf_counter()
        print(f"Time: {end - start:.2f}s/{len(graph.assets)} assets")
        writer = JSONGraphWriter(Path("data/northwind-semantic-v5.json"))
        writer.write(graph)


if __name__ == "__main__":
    unittest.main()
