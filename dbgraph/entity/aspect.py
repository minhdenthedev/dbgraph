from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum


@dataclass
class Aspect:
    """Represent a set of properties that are related to an aspect

    Attributes:
        name: The name of this aspect
    """

    name: str


@dataclass
class SemanticAspect(Aspect):
    """Represent properties related to semantic meaning of the asset

    Attributes:
        description: The natural language description for this asset
        keywords: list of relevant keywords
    """

    description: str
    keywords: list[str]


@dataclass
class RTableSchemaAspect(Aspect):
    """Group of properties relevant to relational databases' table schema

    Attributes:
        pks: list of column names belong to the primary key
        indices: a dictionary which map the table's indices with the columns belong to corresponding indices
    """

    pks: list[str]
    indices: dict[str, list[str]]


@dataclass
class RTableStatisticsAspect(Aspect):
    """Group of properties relevant to relational databases' table statistics

    Attributes:
        num_columns: number of columns
        num_rows: number of rows
    """

    num_columns: int
    num_rows: int


@dataclass
class RColumnSchemaAspect(Aspect):
    """Group of properties relevant to RDB's column schema

    Attributes:
        dtype: data type
        is_pk: whether or not this column belongs to primary key
        is_nullable: whether or not this column is nullable
    """

    dtype: str
    is_pk: bool
    is_nullable: bool


@dataclass
class RNumericalStatistics:
    """Statistics for numerical columns

    Attributes:
        mean: Mean value
        std: Standard deviation
        min: Minimum value
        q2: 2nd quantile
        median: Median value
        q3: 3rd quantile
        max: Maximum value

    """

    mean: float | None = None
    std: float | None = None
    min: float | None = None
    q2: float | None = None
    median: float | None = None
    q3: float | None = None
    max: float | None = None


@dataclass
class RCategoricalStatistics:
    """Statistics for categorical columns

    Attributes:
        value_counts: top 10 most frequent values in a column and
            its corresponding frequency
    """

    value_counts: dict[str, int]


@dataclass
class RTemporalStatistics:
    """Statistics for temporal columns"""
    min_time: datetime | None = None
    max_time: datetime | None = None
    mode_time: datetime | None = None
    num_uniques: int | None = None


@dataclass
class RColumnStatisticsAspect(Aspect):
    """Group of properties relevant to RDB's column statistics

    Attributes:
        non_null_count: Number of non null records
        null_count: Number of null records
        numerical_stats: numerical statistics of this column if its data type is numeric
        categorical_stats: categorical statistics of this column if its data type is string-like
    """

    non_null_count: int
    null_count: int
    numerical_stats: RNumericalStatistics | None = None
    categorical_stats: RCategoricalStatistics | None = None
    temporal_stats: RTemporalStatistics | None = None


class FKBehavior(StrEnum):
    """Defines the behavior of a foreign key when its referenced row changes.

    Attributes:
        CASCADE: Automatically propagates the change to referencing rows.
        SET_NULL: Sets the foreign key value to ``NULL``.
        RESTRICT: Prevents the operation if referencing rows exist.
        NO_ACTION: Does not perform any action on referencing rows.
    """

    CASCADE = "CASCADE"
    SET_NULL = "SET NULL"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO ACTION"


@dataclass
class RForeignKeyAspect(Aspect):
    """Group of properties relevant to foreign keys

    Attributes:
        from_column: the source column
        to_column: referred column
        on_delete: foreign key behavior on delete event
        on_update: foreign key behavior on update event
    """

    from_column: str
    to_column: str
    on_delete: FKBehavior | str
    on_update: FKBehavior | str
