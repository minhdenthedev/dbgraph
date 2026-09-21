import json
from dataclasses import dataclass, asdict
from uuid import UUID

from sqlalchemy import create_engine, select, delete, and_
from sqlalchemy.orm import Session

from dbgraph import Asset, Link, DatabaseGraph, LinkType, AssetType
from dbgraph.entity.aspect import (
    Aspect,
    RTableSchemaAspect,
    RColumnSchemaAspect,
    RTableStatisticsAspect,
    RNumericalStatistics,
    RCategoricalStatistics,
    RTemporalStatistics,
    SemanticAspect,
    RColumnStatisticsAspect,
    RForeignKeyAspect,
)
from dbgraph.persistent.graph_not_found import GraphNotFound
from dbgraph.persistent.graph_persistent import GraphPersistent
from dbgraph.persistent.models.asset_aspect_orm import AssetAspectORM
from dbgraph.persistent.models.asset_orm import AssetORM
from dbgraph.persistent.models.base import Base
from dbgraph.persistent.models.graph_orm import GraphORM
from dbgraph.persistent.models.link_aspect_orm import LinkAspectORM
from dbgraph.persistent.models.link_orm import LinkORM
from dbgraph.utils.serialize import TimeAwareEncoder, TimeAwareDecoder


@dataclass
class ORMGraphPersistent(GraphPersistent):
    persistent_uri: str

    def __post_init__(self):
        self.engine = create_engine(self.persistent_uri)
        Base.metadata.create_all(self.engine)

    def insert_graph(self, graph_id: UUID, graph_name: str):
        orm_graph = GraphORM(graph_id=graph_id, name=graph_name)
        with Session(self.engine) as session:
            session.add(orm_graph)
            session.commit()

    def save_graph(self, graph_id: UUID, graph_name: str, graph: DatabaseGraph):
        self.insert_graph(graph_id, graph_name)
        self.insert_assets(graph.assets, graph_id)
        self.insert_links(graph.links, graph_id)
        for asset in graph.assets:
            self.insert_asset_aspects(asset.aspects, asset.asset_id)
        for link in graph.links:
            self.insert_link_aspects(link.aspects, link.link_id)

    def load_graph(self, graph_id: UUID) -> DatabaseGraph:
        assets = self.get_assets(graph_id)
        links = self.get_links(graph_id)
        for asset in assets:
            asset.aspects = self.get_asset_aspects(asset.asset_id, asset.type)
        for link in links:
            link.aspects = self.get_link_aspects(link.link_id, link.type)
        return DatabaseGraph(assets, links)

    def get_graph_name(self, graph_id: UUID) -> str:
        stmt = select(GraphORM.name).where(GraphORM.graph_id == graph_id)
        with Session(self.engine) as session:
            result = session.scalar(stmt)
        if not result:
            raise GraphNotFound(graph_id)
        return result

    def delete_graph(self, graph_id: UUID):
        stmt = delete(GraphORM).where(GraphORM.graph_id == graph_id)
        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def insert_assets(self, assets: list[Asset], graph_id: UUID):
        orm_assets = [
            AssetORM(
                asset_id=asset.asset_id,
                name=asset.name,
                asset_type=asset.type,
                graph_id=graph_id,
            )
            for asset in assets
        ]
        with Session(self.engine) as session:
            session.add_all(orm_assets)
            session.commit()

    def insert_links(self, links: list[Link], graph_id: UUID):
        orm_links = [
            LinkORM(
                link_id=link.link_id,
                name=link.name,
                link_type=link.type,
                source_id=link.source_id,
                destination_id=link.destination_id,
                graph_id=graph_id,
            )
            for link in links
        ]
        with Session(self.engine) as session:
            session.add_all(orm_links)
            session.commit()

    def delete_assets(self, asset_ids: list[UUID], graph_id: UUID):
        stmt = delete(AssetORM).where(
            and_(AssetORM.asset_id.in_(asset_ids), AssetORM.graph_id == graph_id)
        )
        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def delete_links(self, link_ids: list[UUID], graph_id: UUID):
        stmt = delete(LinkORM).where(
            and_(LinkORM.link_id.in_(link_ids), LinkORM.graph_id == graph_id)
        )
        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def get_links(self, graph_id: UUID) -> list[Link]:
        stmt = select(LinkORM).where(LinkORM.graph_id == graph_id)
        with Session(self.engine) as session:
            rows = session.scalars(stmt).all()
        return [
            Link(
                link_id=row.link_id,
                name=row.name,
                type=LinkType(row.link_type),
                source_id=row.source_id,
                destination_id=row.destination_id,
            )
            for row in rows
        ]

    def get_assets(self, graph_id: UUID) -> list[Asset]:
        stmt = select(AssetORM).where(AssetORM.graph_id == graph_id)
        with Session(self.engine) as session:
            rows = session.scalars(stmt).all()
        return [
            Asset(asset_id=row.asset_id, name=row.name, type=AssetType(row.asset_type))
            for row in rows
        ]

    def insert_asset_aspects(self, aspects: dict[str, Aspect], asset_id: UUID):
        asset_aspects = [
            AssetAspectORM(
                asset_id=asset_id,
                aspect_type=aspect_type,
                json_aspect=json.dumps(asdict(aspect), cls=TimeAwareEncoder),
            )
            for aspect_type, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(asset_aspects)
            session.commit()

    def insert_link_aspects(self, aspects: dict[str, Aspect], link_id: UUID):
        link_aspects = [
            LinkAspectORM(
                link_id=link_id,
                aspect_type=aspect_type,
                json_aspect=json.dumps(asdict(aspect), cls=TimeAwareEncoder),
            )
            for aspect_type, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(link_aspects)
            session.commit()

    def get_asset_aspects(
        self, asset_id: UUID, asset_type: AssetType
    ) -> dict[str, Aspect]:
        stmt = select(AssetAspectORM).where(AssetAspectORM.asset_id == asset_id)
        with Session(self.engine) as session:
            rows = session.scalars(stmt).all()
        answer = {}
        for row in rows:
            aspect_data = json.loads(row.json_aspect, cls=TimeAwareDecoder)
            match row.aspect_type:
                case "schema_properties":
                    match asset_type:
                        case AssetType.RTABLE:
                            aspect = RTableSchemaAspect(**aspect_data)
                        case AssetType.RCOLUMN:
                            aspect = RColumnSchemaAspect(**aspect_data)
                case "statistical_properties":
                    match asset_type:
                        case AssetType.RTABLE:
                            aspect = RTableStatisticsAspect(**aspect_data)
                        case AssetType.RCOLUMN:
                            numerical_aspect = categorical_aspect = temp_aspect = None
                            if aspect_data["numerical_stats"] is not None:
                                numerical_aspect = RNumericalStatistics(
                                    **aspect_data["numerical_stats"]
                                )
                            elif aspect_data["categorical_stats"] is not None:
                                categorical_aspect = RCategoricalStatistics(
                                    **aspect_data["categorical_stats"]
                                )
                            elif aspect_data["temporal_stats"] is not None:
                                temp_aspect = RTemporalStatistics(
                                    **aspect_data["temporal_stats"]
                                )
                            aspect = RColumnStatisticsAspect(
                                name=aspect_data["name"],
                                non_null_count=aspect_data["non_null_count"],
                                null_count=aspect_data["null_count"],
                                categorical_stats=categorical_aspect,
                                numerical_stats=numerical_aspect,
                                temporal_stats=temp_aspect,
                            )
                case "semantic_properties":
                    aspect = SemanticAspect(**aspect_data)
                case _:
                    raise NotImplementedError()
            answer[row.aspect_type] = aspect
        return answer

    def get_link_aspects(self, link_id: UUID, link_type: LinkType) -> dict[str, Aspect]:
        stmt = select(LinkAspectORM).where(LinkAspectORM.link_id == link_id)
        with Session(self.engine) as session:
            rows = session.scalars(stmt).all()
        answer = {}
        for row in rows:
            aspect_data = json.loads(row.json_aspect, cls=TimeAwareDecoder)
            match row.aspect_type:
                case "foreign_key_properties":
                    aspect = RForeignKeyAspect(**aspect_data)
                case _:
                    raise NotImplementedError()
            answer[row.aspect_type] = aspect
        return answer
