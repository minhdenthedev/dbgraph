from dataclasses import dataclass, field

from dbgraph.entity.aspect import Aspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.link_type import LinkType


@dataclass
class Link:
    """
    Represent relationship between two assets.
    """

    link_id: str
    name: str
    type: LinkType
    source: Asset
    destination: Asset
    aspects: dict[str, Aspect] = field(default_factory=dict)
