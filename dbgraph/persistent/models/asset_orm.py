from typing import TYPE_CHECKING, List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbgraph.persistent.models.base import Base
from dbgraph.persistent.models.graph_orm import GraphORM

if TYPE_CHECKING:
    from dbgraph.persistent.models.asset_aspect_orm import AssetAspectORM


class AssetORM(Base):
    __tablename__ = "assets"

    asset_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    asset_type: Mapped[str]
    graph_id: Mapped[UUID] = mapped_column(
        ForeignKey("graphs.graph_id", ondelete="CASCADE", onupdate="CASCADE")
    )

    graph: Mapped[GraphORM] = relationship(back_populates="assets")
    asset_aspects: Mapped[List["AssetAspectORM"]] = relationship(back_populates="asset")
