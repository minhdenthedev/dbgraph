import json
from dataclasses import asdict, dataclass

from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session

from dbgraph.entity.aspect import Aspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.dbgraph import DatabaseGraph
from dbgraph.entity.link import Link
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
        graph_model = GraphModel(
            graph_id=graph_id,
            name=graph_name,
            completed=False
        )
        with Session(self.engine) as session:
            session.add(graph_model)
            session.commit()

    def delete_graph(self, graph_id: str):
        with Session(self.engine) as session:
            session.execute(
                delete(GraphModel).where(
                    GraphModel.graph_id == graph_id
                )
            )
            session.commit()

    def insert_assets(self, assets: list[Asset], graph_id: str):
        """Insert the assets into database"""
        models = [
            AssetModel(
                asset_id=asset.asset_id,
                name=asset.name,
                asset_type=asset.type.value,
                graph_id=graph_id
            )
            for asset in assets
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def insert_asset(self, asset: Asset, graph_id: str):
        """Insert a single asset"""
        model = AssetModel(
            asset_id=asset.asset_id,
            name=asset.name,
            asset_type=asset.type.value,
            graph_id=graph_id
        )
        with Session(self.engine) as session:
            session.add(model)
            session.commit()

    def insert_links(self, links: list[Link], graph_id: str):
        """Insert links into database"""
        models = [
            LinkModel(
                link_id=link.link_id,
                name=link.name,
                link_type=link.type.value,
                source_id=link.source_id,
                destination_id=link.destination_id,
                graph_id=graph_id
            )
            for link in links
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def insert_link(self, link: Link, graph_id: str):
        """Insert a single link into the database"""
        model = LinkModel(
            link_id=link.link_id,
            name=link.name,
            link_type=link.type.value,
            source_id=link.source_id,
            destination_id=link.destination_id,
            graph_id=graph_id
        )
        with Session(self.engine) as session:
            session.add(model)
            session.commit()

    def remove_assets(self, assets_ids: list[str], graph_id: str):
        with Session(self.engine) as session:
            session.execute(
                delete(AssetModel).where(
                    AssetModel.asset_id.in_(assets_ids)
                )
            )
            session.commit()

    def remove_asset(self, asset_id: str, graph_id: str):
        """Remove the asset from the database and return it"""
        with Session(self.engine) as session:
            session.execute(
                delete(AssetModel).where(
                    AssetModel.asset_id == asset_id
                )
            )
            session.commit()

    def remove_links(self, links_ids: list[str], graph_id: str):
        """Remove the links and return them"""
        with Session(self.engine) as session:
            session.execute(
                delete(LinkModel).where(
                    LinkModel.link_id.in_(links_ids)
                )
            )
            session.commit()

    def remove_link(self, link_id: str, graph_id: str):
        """Remove the link and return it"""
        with Session(self.engine) as session:
            session.execute(
                delete(LinkModel).where(
                    LinkModel.link_id == link_id
                )
            )
            session.commit()

    def insert_asset_aspects(
        self, asset_id: str, aspects: dict[str, Aspect]
    ):
        """Insert aspects into asset"""
        models = [
            AssetAspectModel(
                name=name,
                asset_id=asset_id,
                json_aspect=json.dumps(asdict(aspect))
            )
            for name, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def insert_link_aspects(
        self, link_id: str, aspects: dict[str, Aspect]
    ):
        """Insert aspects into link"""
        models = [
            LinkAspectModel(
                name=name,
                link_id=link_id,
                json_aspect=json.dumps(asdict(aspect))
            )
            for name, aspect in aspects.items()
        ]
        with Session(self.engine) as session:
            session.add_all(models)
            session.commit()

    def get_aspects_of_asset(self, asset_id: str) -> dict[str, Aspect]:
        """Get the aspects of an asset"""
        with Session(self.engine) as session:
            models = session.scalars(
                select(AssetAspectModel).where(
                    AssetAspectModel.asset_id == asset_id
                )
            )
            answers: dict[str, Aspect]

    def get_aspects_of_link(self, link_id: str) -> dict[str, Aspect]:
        """Get the aspects of a link"""

    def load_graph(self, graph_id: str, load_aspects: bool = False) -> DatabaseGraph:
        """Load the full database graph"""

    def save_graph(self, graph: DatabaseGraph, graph_id: str):
        """Save the graph into database"""

    def set_graph_state(self, graph_id: str, completed: bool):
        """Mark the graph as completely built and saved in the database or hasn't been finished building yet"""
