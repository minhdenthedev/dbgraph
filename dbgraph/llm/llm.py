from abc import ABC, abstractmethod

from dbgraph.entity.aspect import SemanticAspect
from dbgraph.entity.asset import Asset


class LLM(ABC):
    """Interface for LLMs"""

    @abstractmethod
    def generate_semantic_aspects(
        self, system_prompt: str, user_prompt: str, assets_ids: list[str]
    ) -> dict[str, SemanticAspect]:
        pass
