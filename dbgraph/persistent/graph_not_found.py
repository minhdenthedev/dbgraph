from uuid import UUID


class GraphNotFound(Exception):
    def __init__(self, graph_id: UUID):
        super().__init__(f"Graph with id={str(graph_id)} not found")
