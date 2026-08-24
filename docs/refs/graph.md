> **Module**: dbgraph

`DatabaseGraph` is a convenient data structure that hold information of a database. It is made of two important components:

- a list of `Asset`: Represent data assets, such as SQL or JSON-like (e.g. MongoDB) databases.
- a list of `Link`: Each one represent a relationship between two `Asset`, such as containment (table - column) or foreign keys.

Since `DatabaseGraph` is actually a graph, an `Asset` acts as a vertex and a `Link` acts as an edge in the graph.

::: dbgraph.Asset
::: dbgraph.AssetType
::: dbgraph.Link
::: dbgraph.LinkType
::: dbgraph.DatabaseGraph
