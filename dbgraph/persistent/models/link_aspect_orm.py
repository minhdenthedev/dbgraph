from uuid import UUID

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbgraph.persistent.models.base import Base
from dbgraph.persistent.models.link_orm import LinkORM


class LinkAspectORM(Base):
    __tablename__ = "link_aspects"

    link_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "links.link_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        primary_key=True
    )
    aspect_type: Mapped[str] = mapped_column(primary_key=True)
    json_aspect: Mapped[str]

    link: Mapped[LinkORM] = relationship(back_populates="link_aspects")
