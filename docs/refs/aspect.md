> **Module:** `dbgraph.entity.aspect`

An aspect is a set of properties that are relevant to each other.

For example, an aspect called **statistical aspect** may contain the following
properties: `min`, `max`, `median`, `mean`, and `std`. Another aspect called
**semantic aspect** may contain `description` or `keywords` properties.

Every aspect used within `dbgraph` must extend the base `Aspect` class.

The following aspects are defined in `dbgraph.entity.aspect`:

::: dbgraph.entity.aspect.Aspect
::: dbgraph.entity.aspect.SemanticAspect
::: dbgraph.entity.aspect.RTableSchemaAspect
::: dbgraph.entity.aspect.RTableStatisticsAspect
::: dbgraph.entity.aspect.RColumnSchemaAspect
::: dbgraph.entity.aspect.RNumericalStatistics
::: dbgraph.entity.aspect.RCategoricalStatistics
::: dbgraph.entity.aspect.RColumnStatisticsAspect
::: dbgraph.entity.aspect.FKBehavior
::: dbgraph.entity.aspect.RForeignKeyAspect
