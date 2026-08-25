import os
import unittest
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from dbgraph.descriptor.prompt_templates import COLUMN_QUESTION_PROMPT, COLUMN_SYSTEM_PROMPT, TABLE_QUESTION_PROMPT, TABLE_SYSTEM_PROMPT
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.render.markdown_renderer import MarkdownRenderer
from dbgraph.io.json_graph_writer import JSONGraphWriter

load_dotenv()

from dbgraph.descriptor.langchain_graph_descriptor import LangchainGraphDescriptor
from dbgraph.io.json_graph_loader import JSONGraphLoader


class TestJSONGraphLoader(unittest.TestCase):
    def setUp(self):
        assets = [
            Asset(asset_id="1", name="table-1", type=AssetType.RTABLE),
            Asset(asset_id="2", name="table-2", type=AssetType.RTABLE),
            Asset(asset_id="3", name="table-3", type=AssetType.RTABLE),
            Asset(asset_id="4", name="column-1-1", type=AssetType.RCOLUMN),
            Asset(asset_id="5", name="column-1-2", type=AssetType.RCOLUMN),
            Asset(asset_id="6", name="column-2-1", type=AssetType.RCOLUMN),
            Asset(asset_id="7", name="column-2-2", type=AssetType.RCOLUMN),
            Asset(asset_id="8", name="column-3-1", type=AssetType.RCOLUMN),
            Asset(asset_id="9", name="column-3-2", type=AssetType.RCOLUMN),
        ]
        links = [
            Link(
                link_id="1",
                name="table-1-column-1-1",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[3].asset_id,
            ),
            Link(
                link_id="2",
                name="table-1-column-1-2",
                type=LinkType.CONTAIN,
                source_id=assets[0].asset_id,
                destination_id=assets[4].asset_id,
            ),
            Link(
                link_id="3",
                name="table-2-column-2-1",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[5].asset_id,
            ),
            Link(
                link_id="4",
                name="table-2-column-2-2",
                type=LinkType.CONTAIN,
                source_id=assets[1].asset_id,
                destination_id=assets[6].asset_id,
            ),
            Link(
                link_id="5",
                name="table-3-column-3-1",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[7].asset_id,
            ),
            Link(
                link_id="6",
                name="table-3-column-3-2",
                type=LinkType.CONTAIN,
                source_id=assets[2].asset_id,
                destination_id=assets[8].asset_id,
            ),
            Link(
                link_id="7",
                name="table-1-table-2",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[0].asset_id,
                destination_id=assets[1].asset_id,
            ),
            Link(
                link_id="8",
                name="table-2-table-3",
                type=LinkType.FOREIGN_KEY,
                source_id=assets[1].asset_id,
                destination_id=assets[2].asset_id,
            ),
        ]
        self.dbgraph = DatabaseGraph(assets, links)
        model = ChatOpenAI(
            base_url=os.getenv("LLM_BASE_URL"),
            model=os.getenv("LLM_MODEL", ""),
            api_key=SecretStr(os.getenv("API_KEY", "")),
            extra_body={
                "extra_body": {
                    "enable_thinking": False
                }
            },
        )
        self.descriptor = LangchainGraphDescriptor(
            model=model,
            table_system_prompt=TABLE_SYSTEM_PROMPT,
            table_question_prompt=TABLE_QUESTION_PROMPT,
            column_system_prompt=COLUMN_SYSTEM_PROMPT,
            column_question_prompt=COLUMN_QUESTION_PROMPT,
            max_workers=4,
            markdown_renderer=MarkdownRenderer()
        )


    def test_rfill(self):
        graph = self.descriptor.rfill_semantic_aspects_seq(RDatabaseGraph.from_graph(self.dbgraph))
        writer = JSONGraphWriter(Path("data/northwind-semantic-v5.json"))
        writer.write(graph)



if __name__ == "__main__":
    unittest.main()
