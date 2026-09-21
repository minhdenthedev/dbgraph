from typing import TYPE_CHECKING, List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbgraph.persistent.models.base import Base
from dbgraph.persistent.models.graph_orm import GraphORM

if TYPE_CHECKING:
    from dbgraph.persistent.models.link_aspect_orm import LinkAspectORM


class LinkORM(Base):
    __tablename__ = "links"

    link_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    link_type: Mapped[str]
    source_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "assets.asset_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    destination_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "assets.asset_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    graph_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "graphs.graph_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )

    graph: Mapped[GraphORM] = relationship(back_populates="links")
    link_aspects: Mapped[List["LinkAspectORM"]] = relationship(back_populates="link")
