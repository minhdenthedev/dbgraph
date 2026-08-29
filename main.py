from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from dbgraph.application import Application
from dbgraph.cli import CLI
from dbgraph.config import Config
from dbgraph.descriptor.langchain_graph_descriptor import LangchainGraphDescriptor
from dbgraph.descriptor.prompt_templates import (
    COLUMN_QUESTION_PROMPT,
    COLUMN_SYSTEM_PROMPT,
    TABLE_QUESTION_PROMPT,
    TABLE_SYSTEM_PROMPT,
)
from dbgraph.render.markdown_renderer import MarkdownRenderer

if __name__ == "__main__":
    config = Config.load()
    if config.METADATA_URI is None:
        raise RuntimeError("Metadata URI is not set. Please see `config -h` for more information.")
    if config.MODEL and config.API_KEY and config.OPENAI_BASE_URL:
        model = ChatOpenAI(
            base_url=config.OPENAI_BASE_URL,
            model=config.MODEL,
            api_key=SecretStr(config.API_KEY),
            extra_body={
                "extra_body": {"chat_template_kwargs": {"enable_thinking": False}}
            },
        )
        descriptor = LangchainGraphDescriptor(
            model=model,
            table_system_prompt=TABLE_SYSTEM_PROMPT,
            table_question_prompt=TABLE_QUESTION_PROMPT,
            column_system_prompt=COLUMN_SYSTEM_PROMPT,
            column_question_prompt=COLUMN_QUESTION_PROMPT,
            max_workers=4,
            markdown_renderer=MarkdownRenderer(),
        )
    else:
        descriptor = None
    application = Application(
        source_database_type=config.SOURCE_DATABASE_TYPE,
        graph_persistent_type="sql",
        graph_persistent_uri=config.METADATA_URI,
        descriptor=descriptor
    )
    cli = CLI(application)
    cli.run()
