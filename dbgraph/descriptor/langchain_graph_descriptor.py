from dataclasses import dataclass

from langchain.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage
from langchain_core.messages.human import HumanMessage

from dbgraph import AssetType
from dbgraph.descriptor.graph_descriptor import GraphDescriptor
from dbgraph.entity.aspect import SemanticAspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.render.markdown_renderer import MarkdownRenderer


@dataclass
class LangchainGraphDescriptor(GraphDescriptor):
    """Implementation of `GraphDescriptor` using Langchain"""

    model: BaseChatModel
    table_system_prompt: str
    table_question_prompt: str
    column_system_prompt: str
    column_question_prompt: str
    markdown_renderer: MarkdownRenderer

    def _generate(self, system_prompt: str, question: str) -> str:
        print("Generating...")
        # TODO: time profiling
        response = self.model.invoke(
            [SystemMessage(content=system_prompt), HumanMessage(content=question)]
        )
        print(f"Generated: {question}")
        if response.content is None:
            raise ValueError("Couldn't generate description")
        return str(response.content)

    def _get_sematic_aspect_column(self, asset: Asset, context: RDatabaseGraph) -> SemanticAspect:
        self.markdown_renderer.render(context)
        system_prompt = self.table_system_prompt + "\n" + self.markdown_renderer.get_content()
        question = self.table_question_prompt + " " + asset.name
        description = self._generate(system_prompt, question)
        return SemanticAspect(name=f"{asset.name}_semantic_properties", description=description, keywords=[])


    def _get_semantic_aspect_table(self, asset: Asset, context: RDatabaseGraph) -> SemanticAspect:
        self.markdown_renderer.render(context)
        system_prompt = self.column_system_prompt + "\n" + self.markdown_renderer.get_content()
        question = self.column_question_prompt + " " + asset.name
        description = self._generate(system_prompt, question)
        return SemanticAspect(name=f"{asset.name}_semantic_properties", description=description, keywords=[])

    def get_semantic_aspect(self, asset: Asset, context: RDatabaseGraph) -> SemanticAspect:
        if asset.type == AssetType.RCOLUMN:
            return self._get_sematic_aspect_column(asset, context)
        elif asset.type == AssetType.RTABLE:
            return self._get_semantic_aspect_table(asset, context)
        else:
            raise NotImplementedError("Only support for table and column in relational databases")
