from dataclasses import dataclass

from openai import OpenAI

from dbgraph.llm.llm import LLM


@dataclass
class OAICompatibleLLM(LLM):
    """Implementation of LLM using OAI Compatible API"""

    model: str
    base_url: str
    api_key: str

    def generate(self, system_prompt: str, user_prompt: str) -> str:
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
