from dataclasses import dataclass
from enum import StrEnum


@dataclass
class Aspect:
    """
    Represent a set of properties that are related to an aspect
    """

    name: str


@dataclass
class SemanticAspect(Aspect):
    """Represent properties related to semantic"""

    description: str
    keywords: list[str]


@dataclass
class RTableSchemaAspect(Aspect):
    """
    Group of properties relevant to RDB's table schema
    """

    pks: list[str]
    indices: dict[str, list[str]]


@dataclass
class RTableStatisticsAspect(Aspect):
    """
    Group of properties relevant to RDB's table statistics
    """

    num_columns: int
    num_rows: int


@dataclass
class RColumnSchemaAspect(Aspect):
    """Group of properties relevant to RDB's column schema"""

    dtype: str
    is_pk: bool
    is_nullable: bool


@dataclass
class RNumericalStatistics:
    """Statistics for numerical columns"""

    mean: float | None = None
    std: float | None = None
    min: float | None = None
    q2: float | None = None
    median: float | None = None
    q3: float | None = None
    max: float | None = None


@dataclass
class RCategoricalStatistics:
    """Statistics for categorical columns"""

    value_counts: dict[str, int]


@dataclass
class RColumnStatisticsAspect(Aspect):
    """Group of properties relevant to RDB's column statistics"""

    non_null_count: int
    null_count: int
    numerical_stats: RNumericalStatistics | None = None
    categorical_stats: RCategoricalStatistics | None = None


class FKBehavior(StrEnum):
    CASCADE = "CASCADE"
    SET_NULL = "SET NULL"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO ACTION"


@dataclass
class RForeignKeyAspect(Aspect):
    """Group of properties relevant to foreign keys"""

    from_column: str
    to_column: str
    on_delete: FKBehavior
    on_update: FKBehavior
