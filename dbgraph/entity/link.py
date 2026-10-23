from __future__ import annotations
from dataclasses import dataclass, field
from typing import cast
from uuid import UUID

from dbgraph.entity.aspect import Aspect, RForeignKeyAspect
from dbgraph.entity.link_type import LinkType


@dataclass
class Link:
    """
    Represent relationship between two assets.

    Attributes:
        link_id: ID of this link
        name: name
        type: type of link
        source_id: ID of the source `Asset`
        destination_id: ID of the destination `Asset`
        aspects: properties aspects belong to this link
    """

    link_id: UUID
    name: str
    type: LinkType
    source_id: UUID
    destination_id: UUID
    aspects: dict[str, Aspect] = field(default_factory=dict)

    def to_markdown(self, src_name: str, dst_name: str) -> str:
        match self.type:
            case LinkType.CONTAIN:
                return f"- Column `{dst_name}` belongs to table `{src_name}`\n"
            case LinkType.FOREIGN_KEY:
                fk_aspect = cast(
                    RForeignKeyAspect, self.aspects["foreign_key_properties"]
                )
                return f"- `{src_name}`.`{fk_aspect.from_column}` -> `{dst_name}`.`{fk_aspect.to_column}`\n"

    def __hash__(self) -> int:
        return hash(self.link_id)

    def __eq__(self, value: object, /) -> bool:
        return isinstance(value, Link) and value.link_id == self.link_id
