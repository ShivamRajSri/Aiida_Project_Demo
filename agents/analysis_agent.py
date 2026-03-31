from pathlib import Path
from llm.model_client import ModelClient
from tools.mcp_server import call_tool
import re

PROMPT = Path("config/prompts/analysis_agent.txt").read_text()

class AnalysisAgent:
    def __init__(self):
        self.llm = ModelClient()

    def handle(self, user_input: str) -> str:
        bandgap = self._extract_bandgap_threshold(user_input)
        results = call_tool("query_calculations", bandgap_gt=bandgap)
        augmented = f"{user_input}\n\n[Tool result: {results}]"
        return self.llm.chat(PROMPT, augmented)

    def _extract_bandgap_threshold(self, text: str) -> float | None:
        match = re.search(r"(\d+(\.\d+)?)\s*(eV)?", text)
        return float(match.group(1)) if match else None