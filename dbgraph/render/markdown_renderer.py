from dataclasses import dataclass

from dbgraph import AssetType, LinkType
from dbgraph.entity.aspect import (
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    SemanticAspect,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.render.graph_renderer import GraphRenderer


@dataclass
class MarkdownRenderer(GraphRenderer):
    """Render the graph to Markdown format"""

    categorical_value_max_char: int = 50

    def __post_init__(self):
        self.content = ""

    def _dump_table(self, asset: Asset) -> str:
        if asset.type != AssetType.RTABLE:
            raise TypeError(f"Asset of type {asset.type} is not table type")
        if "semantic_properties" in asset.aspects and isinstance(
            asset.aspects["semantic_properties"], SemanticAspect
        ):
            answer = f"""# Table `{asset.name}`
{asset.aspects["semantic_properties"].description}
- ID: {asset.asset_id}"""
        else:
            answer = f"""# Table `{asset.name}`
- ID: {asset.asset_id}"""
        for aspect_name, aspect in asset.aspects.items():
            if isinstance(aspect, RTableStatisticsAspect):
                answer += f"\n- `{aspect_name}`: {aspect.num_rows} row(s), {aspect.num_columns} columns"
            elif isinstance(aspect, RTableSchemaAspect):
                answer += f"\n- `{aspect_name}`:"
                answer += f"\n\t- Primary keys: {', '.join(aspect.pks)}"
        return answer

    def _dump_column(self, asset: Asset) -> str:
        header = f"""## Column `{asset.name}`"""
        if asset.type != AssetType.RCOLUMN:
            raise TypeError(f"Asset of type {asset.type} is not column type")
        if "semantic_properties" in asset.aspects and isinstance(
            asset.aspects["semantic_properties"], SemanticAspect
        ):
            answer = f"""{asset.aspects["semantic_properties"].description}
- ID: {asset.asset_id}"""
        else:
            answer = f"""- ID: {asset.asset_id}"""
        for aspect_name, aspect in asset.aspects.items():
            if isinstance(aspect, RColumnSchemaAspect):
                answer += f"\n- `{aspect_name}`: dtype={aspect.dtype}, nullable={aspect.is_nullable}"
                if aspect.is_pk:
                    header += "(Primary Key)"
            elif isinstance(aspect, RColumnStatisticsAspect):
                if aspect.numerical_stats is not None:
                    answer += f"\n- Numerical stats: min={aspect.numerical_stats.min}, max={aspect.numerical_stats.max}, mean={aspect.numerical_stats.mean}"
                elif aspect.categorical_stats is not None:
                    answer += "\n- Top 10 Value counts: "
                    for key, value in aspect.categorical_stats.value_counts.items():
                        if len(key) > self.categorical_value_max_char:
                            key = key[: self.categorical_value_max_char] + "..."
                        answer += f"\n\t- {key}: {value}"
        return header + "\n" + answer

    def _dump_fk(self, link: Link, graph: DatabaseGraph) -> str:
        if link.type != LinkType.FOREIGN_KEY:
            raise TypeError(f"Link of type {link.type} is not foreign key type")
        src_name = graph.get_asset(link.source_id).name
        dst_name = graph.get_asset(link.destination_id).name
        if "foreign_key_properties" in link.aspects and isinstance(
            link.aspects["foreign_key_properties"], RForeignKeyAspect
        ):
            aspect = link.aspects["foreign_key_properties"]
            answer = (
                f"- {src_name}.{aspect.from_column} -> {dst_name}.{aspect.to_column}"
            )
        else:
            answer = f"- {src_name} -> {dst_name}"

        return answer

    def render(self, graph: DatabaseGraph) -> str:
        graph = RDatabaseGraph.from_graph(graph)
        tables = graph.get_tables()
        answer = ""
        for table in tables:
            answer += f"\n{self._dump_table(table)}"
            columns = graph.get_columns(table.asset_id)
            for column in columns:
                answer += f"\n{self._dump_column(column)}"
        foreign_keys = graph.get_foreign_keys()
        if len(foreign_keys) > 0:
            answer += "\n# List of Foreign Key Constraints"
            for fk in foreign_keys:
                answer += f"\n{self._dump_fk(fk, graph)}"
        return answer
