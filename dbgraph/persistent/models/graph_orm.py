from typing import List, TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbgraph.persistent.models.base import Base

if TYPE_CHECKING:
    from dbgraph.persistent.models.asset_orm import AssetORM
    from dbgraph.persistent.models.link_orm import LinkORM

class GraphORM(Base):
    __tablename__ = "graphs"

    graph_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]

    assets: Mapped[List["AssetORM"]] = relationship(back_populates="graph")
    links: Mapped[List["LinkORM"]] = relationship(back_populates="graph")

