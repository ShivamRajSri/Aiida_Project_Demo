from pathlib import Path
from llm.model_client import ModelClient
from rag.retriever import retrieve
from tools.mcp_server import call_tool
import re

PROMPT = Path("config/prompts/workflow_agent.txt").read_text()

class WorkflowAgent:
    def __init__(self):
        self.llm = ModelClient()

    def handle(self, user_input: str) -> str:
        context = retrieve(user_input)
        full_prompt = PROMPT + f"\n\nRelevant documentation:\n{context}"

        # Submit a mock calculation
        result = call_tool("submit_calculation",
                           structure=self._extract_structure(user_input),
                           parameters={"calculation": "relax", "ecutwfc": 60})

        augmented = f"{user_input}\n\n[Tool result: {result}]"
        return self.llm.chat(full_prompt, augmented)

    def _extract_structure(self, text: str) -> str:
        # Simple heuristic: look for a known material name
        for material in ["Si", "GaN", "TiO2", "Fe", "Al"]:
            if material.lower() in text.lower():
                return material
        return "unknown_structure"