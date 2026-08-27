import os
import unittest

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from dbgraph.application import Application
from dbgraph.descriptor.langchain_graph_descriptor import LangchainGraphDescriptor
from dbgraph.descriptor.prompt_templates import (
    COLUMN_QUESTION_PROMPT,
    COLUMN_SYSTEM_PROMPT,
    TABLE_QUESTION_PROMPT,
    TABLE_SYSTEM_PROMPT,
)
from dbgraph.render.markdown_renderer import MarkdownRenderer

load_dotenv()


class TestApplication(unittest.TestCase):
    def setUp(self):
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
        self.application = Application(
            descriptor=self.descriptor,
            graph_persistent_type="sql",
            graph_persistent_uri="sqlite:///data/northwind-graph.db",
            source_database_type="sql",
        )

    def test_build_graph(self):
        self.application.build_graph(
            name="northwind-graph",
            database_uri="sqlite:///data/northwind.db",
            fill_semantic=True,
        )


if __name__ == "__main__":
    unittest.main()
