from pathlib import Path
import re

from llm.model_client import ModelClient
from rag.retriever import retrieve
from tools.mcp_server import call_tool


PROMPT = Path(
    "config/prompts/workflow_agent.txt"
).read_text()


class WorkflowAgent:
    def __init__(self):
        self.llm = ModelClient()

    def handle(self, user_input: str) -> str:
        context = retrieve(user_input)

        # Only submit when the user explicitly asks to submit/run
        submission_words = [
            "submit",
            "execute",
            "launch",
            "start the calculation",
            "run the calculation",
        ]

        should_submit = any(
            word in user_input.lower()
            for word in submission_words
        )

        if not should_submit:
            augmented = (
                f"{user_input}\n\n"
                f"[Relevant documentation]\n"
                f"{context}"
            )

            return self.llm.chat(PROMPT, augmented)

        result = call_tool(
            "submit_calculation",
            structure=self._extract_structure(user_input),
            parameters={
                "calculation": "relax",
                "ecutwfc": 60,
            },
        )

        augmented = (
            f"{user_input}\n\n"
            f"[Relevant documentation]\n{context}\n\n"
            f"[Tool result]\n{result}"
        )

        return self.llm.chat(PROMPT, augmented)

    def _extract_structure(self, text: str) -> str:
        for material in ["Si", "GaN", "TiO2"]:
            if material.lower() in text.lower():
                return material

        return "unknown_structure"