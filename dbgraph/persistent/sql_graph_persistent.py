from dataclasses import asdict, dataclass

from sqlalchemy import create_engine, delete, select, update
from sqlalchemy.orm import Session

from dbgraph.entity.aspect import (
    Aspect,
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
from dbgraph.persistent.graph_persistent import GraphPersistent
from dbgraph.persistent.models import (
    AssetAspectModel,
    AssetModel,
    Base,
    GraphModel,
    LinkAspectModel,
    LinkModel,
)


@dataclass
class SQLGraphPersistent(GraphPersistent):
    """Implementation of GraphPersistent using SQL databases and SQLAlchemy"""

    db_uri: str

    def __post_init__(self):
        self.engine = create_engine(self.db_uri)
        Base.metadata.create_all(bind=self.engine)

    def create_graph(self, graph_id: str, graph_name: str):
        graph_model = GraphModel(graph_id=graph_id, name=graph_name, completed=False)
        with Session(self.engine) as session:
            session.add(graph_model)
            session.commit()

    def delete_graph(self, graph_id: str):
        with Session(self.engine) as session:
            session.execute(delete(GraphModel).where(GraphModel.graph_id == graph_id))
            session.commit()

    def insert_assets(self, assets: list[Asset], graph_id: str):
        """Insert the assets into database"""
        models = [
            AssetModel(
                asset_id=asset.asset_id,
                name=asset.name,
                asset_type=asset.type.value,
                graph_id=graph_id,
            )
            for asset in assets
        ]
        aspects = []
        for asset in assets:
            for aspect_type, aspect in asset.aspects.items():
                aspect = AssetAspectModel(
                    asset_id=asset.asset_id,
                    name=aspect.name,
                    type=aspect_type,
                    json_aspect=asdict(aspect),
                )
                aspects.append(aspect)
        with Session(self.engine) as session:
            session.add_all(models)
            session.add_all(aspects)
            session.commit()

    def insert_asset(self, asset: Asset, graph_id: str):
        """Insert a single asset"""
        model = AssetModel(
            asset_id=asset.asset_id,
            name=asset.name,
            asset_type=asset.type.value,
            graph_id=graph_id,
        )
        with Session(self.engine) as session:
            session.add(model)
            session.commit()
        self.insert_asset_aspects(asset.asset_id, asset.aspects)

    def insert_links(self, links: list[Link], graph_id: str):
        """Insert links into database"""
        models = [
            LinkModel(
                link_id=link.link_id,
                name=link.name,
                link_type=link.type.value,
                source_id=link.source_id,
                destination_id=link.destination_id,
                graph_id=graph_id,
            )
            for link in links
        ]
        aspects = []
        for link in links:
            for aspect_type, aspect in link.aspects.items():
                link_aspect = LinkAspectModel(
                    link_id=link.link_id,
                    name=aspect.name,
                    type=aspect_type,
                    json_aspect=asdict(aspect),
                )
                aspects.append(link_aspect)
        with Session(self.engine) as session:
            session.add_all(models)
            session.add_all(aspects)
            session.commit()

    def insert_link(self, link: Link, graph_id: str):
        """Insert a single link into the database"""
        model = LinkModel(
            link_id=link.link_id,
            name=link.name,
            link_type=link.type.value,
            source_id=link.source_id,
            destination_id=link.destination_id,
            graph_id=graph_id,
        )
        with Session(self.engine) as session:
            session.add(model)
            session.commit()
        self.insert_link_aspects(link.link_id, link.aspects)

    def get_link(self, link_id: str, graph_id: str) -> Link:
        with Session(self.engine) as session:
            model = session.scalar(
                select(LinkModel).where(
                    LinkModel.link_id == link_id and LinkModel.graph_id == graph_id
                )
            )
        if model is None:
            raise KeyError(f"Link with id={link_id} not found in graph={graph_id}")
        aspects = self.get_aspects_of_link(link_id)
        return Link(
            link_id=link_id,
            name=model.name,
            source_id=model.source_id,
            destination_id=model.destination_id,
            aspects=aspects,
            type=LinkType(model.link_type),
        )

    def remove_assets(self, assets_ids: list[str], graph_id: str):
        with Session(self.engine) as session:
            session.execute(
                delete(AssetModel).where(AssetModel.asset_id.in_(assets_ids))
            )
            session.commit()

    def remove_asset(self, asset_id: str, graph_id: str):
        """Remove the asset from the database and return it"""
        with Session(self.engine) as session:
            session.execute(delete(AssetModel).where(AssetModel.asset_id == asset_id))
            session.commit()

    def get_asset(self, asset_id: str, graph_id: str) -> Asset:
        with Session(self.engine) as session:
            model = session.scalar(
                select(AssetModel).where(
                    AssetModel.asset_id == asset_id and AssetModel.graph_id == graph_id
                )
            )
        if model is None:
            raise KeyError(f"Asset with id={asset_id} not found in graph={graph_id}")
        aspects = self.get_aspects_of_asset(asset_id)
        return Asset(
            asset_id=asset_id,
            name=model.name,
            type=AssetType(model.asset_type),
            aspects=aspects,
        )

    def remove_links(self, links_ids: list[str], graph_id: str):
        """Remove the links and return them"""
        with Session(self.engine) as session:
            session.execute(delete(LinkModel).where(LinkModel.link_id.in_(links_ids)))
            session.commit()

    def remove_link(self, link_id: str, graph_id: str):
        """Remove the link and return it"""
        with Session(self.engine) as session:
            session.execute(delete(LinkModel).where(LinkModel.link_id == link_id))
            session.commit()

    def insert_asset_aspects(self, asset_id: str, aspects: dict[str, Aspect]):
        """Insert aspects into asset"""
        models = [
            AssetAspectModel(
                name=aspect.name,
                type=aspect_type,
                asset_id=asset_id,
                json_aspect=asdict(aspect),
            )
            for aspect_type, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def insert_link_aspects(self, link_id: str, aspects: dict[str, Aspect]):
        """Insert aspects into link"""
        models = [
            LinkAspectModel(
                name=aspect.name,
                type=aspect_type,
                link_id=link_id,
                json_aspect=asdict(aspect),
            )
            for aspect_type, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def _parse_asset_aspect_model(
        self, model: AssetAspectModel, asset_type: AssetType
    ) -> Aspect:
        """Turn SQL Alchemy model to Aspect"""
        json_aspect = model.json_aspect
        match model.type:
            case "schema_properties":
                if asset_type == AssetType.RTABLE:
                    aspect = RTableSchemaAspect(**json_aspect)
                elif asset_type == AssetType.RCOLUMN:
                    aspect = RColumnSchemaAspect(**json_aspect)
                else:
                    raise NotImplementedError()
            case "statistical_properties":
                if asset_type == AssetType.RTABLE:
                    aspect = RTableStatisticsAspect(**json_aspect)
                elif asset_type == AssetType.RCOLUMN:
                    if json_aspect["numerical_stats"] is not None:
                        numerical_aspect = RNumericalStatistics(
                            **json_aspect["numerical_stats"]
                        )
                        categorical_aspect = None
                    elif json_aspect["categorical_stats"] is not None:
                        categorical_aspect = RCategoricalStatistics(
                            **json_aspect["categorical_stats"]
                        )
                        numerical_aspect = None
                    else:
                        raise RuntimeError(
                            "Neither categorical or numerical stats exists"
                        )
                    aspect = RColumnStatisticsAspect(
                        name=json_aspect["name"],
                        non_null_count=json_aspect["non_null_count"],
                        null_count=json_aspect["null_count"],
                        categorical_stats=categorical_aspect,
                        numerical_stats=numerical_aspect,
                    )
                else:
                    raise NotImplementedError()
            case "semantic_properties":
                aspect = SemanticAspect(**json_aspect)
            case _:
                raise NotImplementedError()
        return aspect

    def get_aspects_of_asset(self, asset_id: str) -> dict[str, Aspect]:
        """Get the aspects of an asset"""
        with Session(self.engine) as session:
            models = session.scalars(
                select(AssetAspectModel).where(AssetAspectModel.asset_id == asset_id)
            )
            asset = session.scalar(
                select(AssetModel).where(AssetModel.asset_id == asset_id)
            )
            if asset is None:
                raise KeyError(f"Asset with id={asset_id} not found!")
            asset_type = AssetType(asset.asset_type)
            answers: dict[str, Aspect] = {}
            for model in models:
                answers[model.type] = self._parse_asset_aspect_model(model, asset_type)
            return answers

    def _parse_link_aspect_model(self, model: LinkAspectModel) -> Aspect:
        """Turn SQL Alchemy model to Link Aspect"""
        json_aspect = model.json_aspect
        match model.type:
            case "foreign_key_properties":
                aspect = RForeignKeyAspect(**json_aspect)
            case _:
                raise NotImplementedError()
        return aspect

    def get_aspects_of_link(self, link_id: str) -> dict[str, Aspect]:
        """Get the aspects of a link"""
        with Session(self.engine) as session:
            models = session.scalars(
                select(LinkAspectModel).where(LinkAspectModel.link_id == link_id)
            )
            link = session.scalar(select(LinkModel).where(LinkModel.link_id == link_id))
            if link is None:
                raise KeyError(f"Link with id={link_id} not found!")
            answers: dict[str, Aspect] = {}
            for model in models:
                answers[model.type] = self._parse_link_aspect_model(model)
            return answers

    def get_assets(self, graph_id: str) -> list[Asset]:
        with Session(self.engine) as session:
            models = session.scalars(
                select(AssetModel).where(AssetModel.graph_id == graph_id)
            )
            assets = []
            for model in models:
                aspects = {}
                for aspect_model in model.asset_aspects:
                    aspects[aspect_model.type] = self._parse_asset_aspect_model(
                        aspect_model, AssetType(model.asset_type)
                    )
                asset = Asset(
                    asset_id=model.asset_id,
                    name=model.name,
                    type=AssetType(model.asset_type),
                    aspects=aspects,
                )
                assets.append(asset)
        return assets

    def get_links(self, graph_id: str) -> list[Link]:
        with Session(self.engine) as session:
            models = session.scalars(
                select(LinkModel).where(LinkModel.graph_id == graph_id)
            )
            links = []
            for model in models:
                aspects = {}
                for aspect_model in model.link_aspects:
                    aspects[aspect_model.type] = self._parse_link_aspect_model(
                        aspect_model
                    )
                link = Link(
                    link_id=model.link_id,
                    name=model.name,
                    type=LinkType(model.link_type),
                    aspects=aspects,
                    source_id=model.source_id,
                    destination_id=model.destination_id,
                )
                links.append(link)
        return links

    def load_graph(self, graph_id: str) -> DatabaseGraph:
        """Load the full database graph"""
        links = self.get_links(graph_id)
        assets = self.get_assets(graph_id)
        return DatabaseGraph(assets, links)

    def save_graph(self, graph: DatabaseGraph, graph_id: str):
        """Save the graph into database"""

        self.insert_assets(graph.assets, graph_id)
        self.insert_links(graph.links, graph_id)

    def set_graph_state(self, graph_id: str, completed: bool):
        """Mark the graph as completely built and saved in the database or hasn't been finished building yet"""
        stmt = (
            update(GraphModel)
            .where(GraphModel.graph_id == graph_id)
            .values(completed=completed)
        )
        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def get_graph_info(self, graph_id: str) -> tuple[str, str, bool]:
        with Session(self.engine) as session:
            model = session.scalar(
                select(GraphModel).where(GraphModel.graph_id == graph_id)
            )
            if model is None:
                raise KeyError(f"Graph with id={graph_id} not found")
            return model.graph_id, model.name, model.completed
