from dataclasses import dataclass, field
from typing import cast

from dbgraph.entity.aspect import Aspect, RForeignKeyAspect
from dbgraph.entity.link_type import LinkType


@dataclass
class Link:
    """
    Represent relationship between two assets.
    """

    link_id: str
    name: str
    type: LinkType
    source_id: str
    destination_id: str
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
