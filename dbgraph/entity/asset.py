from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID

from dbgraph.entity.aspect import (
    Aspect,
)
from dbgraph.entity.asset_type import AssetType


@dataclass
class Asset:
    """
    Represent a data asset, such as a table in SQL databases or a document in MongoDB.

    It acts as a vertex in the graph.

    Attributes:
        asset_id: ID of this asset
        name: original name of this asset
        type: type of asset
        aspects: properties aspects belong to this asset
    """

    asset_id: UUID
    name: str
    type: AssetType
    aspects: dict[str, Aspect] = field(default_factory=dict)

    def __hash__(self) -> int:
        return hash(self.asset_id)

    def __eq__(self, value: object, /) -> bool:
        return isinstance(value, Asset) and value.asset_id == self.asset_id
