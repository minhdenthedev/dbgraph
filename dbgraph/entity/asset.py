from dataclasses import asdict, dataclass, field

from dbgraph.entity.aspect import (
    Aspect,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    SemanticAspect,
)
from dbgraph.entity.asset_type import AssetType


@dataclass
class Asset:
    """
    Represent a data asset, such as a table in RDBMS or a document in MongoDB. It is a node with type Asset in the graph.
    """

    asset_id: str
    name: str
    type: AssetType
    aspects: dict[str, Aspect] = field(default_factory=dict)

    def _table_markdown(self) -> str:
        markdown = f"## Table: `{self.name}`\n"
        kws_str = ""
        if "semantic_properties" in self.aspects and isinstance(
            self.aspects["semantic_properties"], SemanticAspect
        ):
            markdown += f"{self.aspects['semantic_properties'].description}\n\n"
            kws_str = ", ".join(self.aspects["semantic_properties"].keywords)
        markdown += f"- ID: {self.asset_id}\n"
        if kws_str.strip() != "":
            markdown += f"- Keywords: {kws_str}"
        if "schema_properties" in self.aspects and isinstance(
            self.aspects["schema_properties"], RTableSchemaAspect
        ):
            pks_str = ", ".join([pk for pk in self.aspects["schema_properties"].pks])
            markdown += f"- Primary Keys: {pks_str}.\n"
        if "statistical_properties" in self.aspects and isinstance(
            self.aspects["statistical_properties"], RTableStatisticsAspect
        ):
            nrows = self.aspects["statistical_properties"].num_rows
            ncols = self.aspects["statistical_properties"].num_columns
            markdown += f"- Shape: {nrows} row(s), {ncols} column(s).\n"
        return markdown

    def _column_markdown(self) -> str:
        markdown = f"### Column: `{self.name}`\n"
        kws_str = ""
        if "semantic_properties" in self.aspects and isinstance(
            self.aspects["semantic_properties"], SemanticAspect
        ):
            markdown += f"{self.aspects['semantic_properties'].description}\n\n"
            kws_str = ", ".join(self.aspects["semantic_properties"].keywords)
        markdown += f"- ID: {self.asset_id}\n"

        if kws_str.strip() != "":
            markdown += f"- Keywords: {kws_str}"
        if "schema_properties" in self.aspects and isinstance(
            self.aspects["schema_properties"], RColumnSchemaAspect
        ):
            markdown += f"- Data type: {self.aspects['schema_properties'].dtype}\n"
            markdown += f"- Is Primary Key: {self.aspects['schema_properties'].is_pk}\n"
            markdown += (
                f"- Is nullable: {self.aspects['schema_properties'].is_nullable}\n"
            )
        if "statistical_properties" in self.aspects and isinstance(
            self.aspects["statistical_properties"], RColumnStatisticsAspect
        ):
            rnumeric_stats = self.aspects["statistical_properties"].numerical_stats
            rcategorical_stats = self.aspects[
                "statistical_properties"
            ].categorical_stats
            non_null_count = self.aspects["statistical_properties"].non_null_count
            null_count = self.aspects["statistical_properties"].null_count
            markdown += f"- Non null count: {non_null_count}\n"
            markdown += f"- Null count: {null_count}\n"
            if rnumeric_stats:
                markdown += f"- Numerical statistics: {asdict(rnumeric_stats)}\n"
            if rcategorical_stats:
                markdown += f"- Categorical statistics: {asdict(rcategorical_stats)}\n"

        return markdown

    def to_markdown(self) -> str:
        """Describe this asset using Markdown"""
        match self.type:
            case AssetType.RTABLE:
                return self._table_markdown()
            case AssetType.RCOLUMN:
                return self._column_markdown()
            case _:
                raise NotImplementedError("Unsupported asset type")
