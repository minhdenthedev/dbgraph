import json
from dataclasses import dataclass

from openai import OpenAI

from dbgraph.entity.aspect import SemanticAspect
from dbgraph.entity.asset import Asset
from dbgraph.llm.llm import LLM


@dataclass
class OAICompatibleLLM(LLM):
    """Implementation of LLM using OAI Compatible API"""

    model: str
    base_url: str
    api_key: str

    def _generate(self, system_prompt: str, user_prompt: str) -> str:
        client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            extra_body={
                "extra_body": {"chat_template_kwargs": {"enable_thinking": False}}
            },
        )
        return response.choices[0].message.content or ""

    def generate_semantic_aspects(
        self, system_prompt: str, user_prompt: str, assets_ids: list[str]
    ) -> dict[str, SemanticAspect]:
        s = self._generate(system_prompt, user_prompt)
        data = json.loads(s) if s else {}
        parsed = {
            k: SemanticAspect(
                name=f"{name}_semantic",
                description=v["description"],
                keywords=v["keywords"],
            )
            for k, (name, v) in zip(assets_ids, data.items())
        }
        return parsed
