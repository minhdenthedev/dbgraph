import json
from dataclasses import dataclass
from pathlib import Path

from dbgraph.entity.aspect import (
    RCategoricalStatistics,
    RColumnSchemaAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
    RNumericalStatistics,
    RTableSchemaAspect,
    RTableStatisticsAspect,
    SemanticAspect,
)
from dbgraph.entity.asset import Asset
from dbgraph.entity.asset_type import AssetType
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
from dbgraph.entity.link_type import LinkType
from dbgraph.io.graph_loader import GraphLoader


@dataclass
class JSONGraphLoader(GraphLoader):
    json_path: Path

    def load(self) -> DatabaseGraph:
        with self.json_path.open("r") as f:
            data = json.load(f)
            assets_data = data["assets"]
            links_data = data["links"]
        assets = []
        links = []
        for data in assets_data:
            if data["type"] == "table":
                asset = self._parse_table_asset(data)
            elif data["type"] == "column":
                asset = self._parse_column_asset(data)
            else:
                raise NotImplementedError(f"Invalid asset type '{data['type']}'")
            assets.append(asset)
        for data in links_data:
            if data["type"] == "contain":
                link = self._parse_contain_link(data)
            elif data["type"] == "foreign-key":
                link = self._parse_fk_link(data)
            else:
                raise NotImplementedError(f"Invalid link type '{data['type']}'")
            links.append(link)
        return DatabaseGraph(assets, links)

    def _parse_fk_link(self, data: dict) -> Link:
        fk_data = data["aspects"]["foreign_key_properties"]
        fk_aspect = RForeignKeyAspect(
            name=fk_data["name"],
            from_column=fk_data["from_column"],
            to_column=fk_data["to_column"],
            on_delete=fk_data["on_delete"],
            on_update=fk_data["on_update"],
        )
        return Link(
            link_id=data["link_id"],
            name=data["name"],
            type=LinkType.FOREIGN_KEY,
            source_id=data["source_id"],
            destination_id=data["destination_id"],
            aspects={"foreign_key_properties": fk_aspect},
        )

    def _parse_contain_link(self, data: dict) -> Link:
        return Link(
            link_id=data["link_id"],
            name=data["name"],
            type=LinkType.CONTAIN,
            source_id=data["source_id"],
            destination_id=data["destination_id"],
        )

    def _parse_table_asset(self, data: dict) -> Asset:
        aspects_data = data["aspects"]
        aspects = {}
        if "schema_properties" in aspects_data:
            properties = aspects_data["schema_properties"]
            aspects["schema_properties"] = RTableSchemaAspect(
                name=properties["name"],
                pks=properties["pks"],
                indices=properties["indices"],
            )
        if "statistical_properties" in aspects_data:
            properties = aspects_data["statistical_properties"]
            aspects["statistical_properties"] = RTableStatisticsAspect(
                name=properties["name"],
                num_columns=properties["num_columns"],
                num_rows=properties["num_rows"],
            )
        if "semantic_properties" in aspects_data:
            properties = aspects_data["semantic_properties"]
            aspects["semantic_properties"] = SemanticAspect(
                name=properties["name"],
                description=properties["description"],
                keywords=properties["keywords"],
            )
        return Asset(
            asset_id=data["asset_id"],
            name=data["name"],
            type=AssetType.RTABLE,
            aspects=aspects,
        )

    def _parse_column_asset(self, data: dict) -> Asset:
        aspects_data = data["aspects"]
        aspects = {}
        if "schema_properties" in aspects_data:
            properties = aspects_data["schema_properties"]
            aspects["schema_properties"] = RColumnSchemaAspect(
                name=properties["name"],
                dtype=properties["dtype"],
                is_pk=properties["is_pk"],
                is_nullable=properties["is_nullable"],
            )
        if "statistical_properties" in aspects_data:
            properties = aspects_data["statistical_properties"]
            numerical_stats = properties["numerical_stats"]
            categorical_stats = properties["categorical_stats"]
            rnumerical_stats = rcategorical_stats = None
            if numerical_stats:
                rnumerical_stats = RNumericalStatistics(
                    mean=numerical_stats["mean"],
                    std=numerical_stats["std"],
                    min=numerical_stats["min"],
                    q2=numerical_stats["q2"],
                    median=numerical_stats["median"],
                    q3=numerical_stats["q3"],
                    max=numerical_stats["max"],
                )
            if categorical_stats:
                rcategorical_stats = RCategoricalStatistics(
                    value_counts=categorical_stats["value_counts"]
                )
            aspects["statistical_properties"] = RColumnStatisticsAspect(
                name=properties["name"],
                non_null_count=properties["non_null_count"],
                null_count=properties["null_count"],
                numerical_stats=rnumerical_stats,
                categorical_stats=rcategorical_stats,
            )
        if "semantic_properties" in aspects_data:
            properties = aspects_data["semantic_properties"]
            aspects["semantic_properties"] = SemanticAspect(
                name=properties["name"],
                description=properties["description"],
                keywords=properties["keywords"],
            )

        return Asset(
            asset_id=data["asset_id"],
            name=data["name"],
            type=AssetType.RCOLUMN,
            aspects=aspects,
        )
