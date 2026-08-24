from enum import StrEnum


class AssetType(StrEnum):
    """Type of `Asset`.

    Attributes:
        table: table in SQL databases
        column: column in SQL databases
    """

    RTABLE = "table"
    RCOLUMN = "column"
