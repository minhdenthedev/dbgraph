from enum import StrEnum


class LinkType(StrEnum):
    """Type of link.

    Attributes:
        foreign-key: Foreign key constraint
        contain: containment relationship (table - columns)
    """

    FOREIGN_KEY = "foreign-key"
    CONTAIN = "contain"
