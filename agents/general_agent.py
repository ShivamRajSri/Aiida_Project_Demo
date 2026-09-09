from pathlib import Path

from llm.model_client import ModelClient
from rag.retriever import retrieve


PROMPT = Path(
    "config/prompts/general_agent.txt"
).read_text()


class GeneralAgent:
    def __init__(self):
        self.llm = ModelClient()

    def handle(self, user_input: str) -> str:
        context = retrieve(user_input)

        augmented = (
            f"{user_input}\n\n"
            f"[Relevant documentation context]\n"
            f"{context}"
        )

        return self.llm.chat(PROMPT, augmented)