from sqlalchemy import (
    JSON,
    Boolean,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class GraphModel(Base):
    __tablename__ = "graphs"

    graph_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    assets: Mapped[list["AssetModel"]] = relationship(
        back_populates="graph",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    links: Mapped[list["LinkModel"]] = relationship(
        back_populates="graph",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class AssetModel(Base):
    __tablename__ = "assets"

    asset_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    asset_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    graph_id: Mapped[str] = mapped_column(
        ForeignKey(
            "graphs.graph_id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    graph: Mapped["GraphModel"] = relationship(
        back_populates="assets",
    )

    outgoing_links: Mapped[list["LinkModel"]] = relationship(
        foreign_keys="LinkModel.source_id",
        back_populates="source",
        cascade="all, delete-orphan",
    )

    incoming_links: Mapped[list["LinkModel"]] = relationship(
        foreign_keys="LinkModel.destination_id",
        back_populates="destination",
        cascade="all, delete-orphan",
    )

    asset_aspects: Mapped[list["AssetAspectModel"]] = relationship(
        back_populates="asset",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class LinkModel(Base):
    __tablename__ = "links"

    link_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    link_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    source_id: Mapped[str] = mapped_column(
        ForeignKey(
            "assets.asset_id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    destination_id: Mapped[str] = mapped_column(
        ForeignKey(
            "assets.asset_id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    graph_id: Mapped[str] = mapped_column(
        ForeignKey(
            "graphs.graph_id",
            ondelete="CASCADE",
        ),
        nullable=False,
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
        back_populates="links",
    )

    link_aspects: Mapped[list["LinkAspectModel"]] = relationship(
        back_populates="link",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class AssetAspectModel(Base):
    __tablename__ = "asset_aspects"

    asset_id: Mapped[str] = mapped_column(
        ForeignKey(
            "assets.asset_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        primary_key=True,
    )

    type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    json_aspect: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    asset: Mapped["AssetModel"] = relationship(
        back_populates="asset_aspects",
    )


class LinkAspectModel(Base):
    __tablename__ = "link_aspects"

    link_id: Mapped[str] = mapped_column(
        ForeignKey(
            "links.link_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        primary_key=True,
    )

    type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    json_aspect: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    link: Mapped["LinkModel"] = relationship(
        back_populates="link_aspects",
    )
