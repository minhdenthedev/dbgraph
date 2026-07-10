from dataclasses import dataclass, field

from dbgraph.entity.aspect import Aspect
from dbgraph.entity.asset_type import AssetType


@dataclass
class Asset:
    """
    Represent a data asset, such as a table in RDBMS or a document in MongoDB. It is a node with type Asset in the graph.
    """

    asset_id: str
    name: str
    type: AssetType
    aspects: dict[str, Aspect] = field(default_factory=dict)
