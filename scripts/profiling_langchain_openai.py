import os
import time

from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()


model = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    model=os.getenv("LLM_MODEL", ""),
    api_key=SecretStr(os.getenv("API_KEY", "")),
    extra_body={"extra_body": {"chat_template_kwargs": {"enable_thinking": False}}},
)
start = time.perf_counter()
response = model.invoke([HumanMessage("Hello. Who are you? Answer me in 3 words.")])
print("Question: Hello. Who are you? Answer me in 3 words.")
print(response.content)
end = time.perf_counter()
print(f"Time: {end - start:.2f}s")
