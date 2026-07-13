from abc import ABC, abstractmethod


class LLM(ABC):
    """Interface for LLMs"""

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        pass
