from abc import ABC, abstractmethod

from dbgraph.entity.aspect import SemanticAspect


class LLM(ABC):
    """Interface for LLMs"""

    @abstractmethod
    def generate_semantic_aspects(self, prompt: str) -> dict[str, SemanticAspect]:
        pass
