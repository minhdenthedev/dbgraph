from uuid import UUID

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbgraph.persistent.models.asset_orm import AssetORM
from dbgraph.persistent.models.base import Base


class AssetAspectORM(Base):
    __tablename__ = "asset_aspects"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.asset_id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    aspect_type: Mapped[str] = mapped_column(primary_key=True)
    json_aspect: Mapped[str]

    asset: Mapped[AssetORM] = relationship(back_populates="asset_aspects")
