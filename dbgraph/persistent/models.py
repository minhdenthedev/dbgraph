from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class GraphModel(Base):
    __tablename__ = "graphs"

    graph_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    completed: Mapped[bool] = mapped_column(default=False)

    assets: Mapped[list["AssetModel"]] = relationship(
        back_populates="graph",
        cascade="all, delete-orphan",
    )

    links: Mapped[list["LinkModel"]] = relationship(
        back_populates="graph",
        cascade="all, delete-orphan",
    )


class AssetModel(Base):
    __tablename__ = "assets"

    asset_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    asset_type: Mapped[str] = mapped_column(String(30))

    graph_id: Mapped[str] = mapped_column(
        ForeignKey("graphs.graph_id", ondelete="CASCADE"),
        index=True,
    )

    graph: Mapped["GraphModel"] = relationship(
        back_populates="assets"
    )


class LinkModel(Base):
    __tablename__ = "links"

    link_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    link_type: Mapped[str] = mapped_column(String(30))

    source_id: Mapped[str] = mapped_column(
        ForeignKey("assets.asset_id", ondelete="CASCADE"),
        index=True,
    )

    destination_id: Mapped[str] = mapped_column(
        ForeignKey("assets.asset_id", ondelete="CASCADE"),
        index=True,
    )

    graph_id: Mapped[str] = mapped_column(
        ForeignKey("graphs.graph_id", ondelete="CASCADE"),
        index=True,
    )

    source: Mapped["AssetModel"] = relationship(
        foreign_keys=[source_id],
        back_populates="outgoing_links",
    )

    destination: Mapped["AssetModel"] = relationship(
        foreign_keys=[destination_id],
        back_populates="incoming_links",
    )

    graph: Mapped["GraphModel"] = relationship(
        back_populates="links"
    )


class AssetAspectModel(Base):
    __tablename__ = "asset_aspects"
    name: Mapped[str] = mapped_column(primary_key=True)
    asset_id: Mapped[str] = mapped_column(
        ForeignKey("assets.asset_id", ondelete="CASCADE"), primary_key=True
    )
    json_aspect: Mapped[str] = mapped_column(Text)

    asset: Mapped["AssetModel"] = relationship(back_populates="asset_aspects")


class LinkAspectModel(Base):
    __tablename__ = "link_aspects"
    name: Mapped[str] = mapped_column(primary_key=True)
    link_id: Mapped[str] = mapped_column(ForeignKey("links.link_id", ondelete="CASCADE"), primary_key=True)
    json_aspect: Mapped[str] = mapped_column(Text)

    link: Mapped["LinkModel"] = relationship(back_populates="link_aspects")
