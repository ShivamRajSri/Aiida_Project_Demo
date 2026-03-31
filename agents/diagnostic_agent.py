from pathlib import Path
from llm.model_client import ModelClient
from tools.mcp_server import call_tool
import re

PROMPT = Path("config/prompts/diagnostic_agent.txt").read_text()

class DiagnosticAgent:
    def __init__(self):
        self.llm = ModelClient()

    def handle(self, user_input: str) -> str:
        pk   = self._extract_pk(user_input)
        log  = call_tool("get_calculation_log", pk=pk)
        augmented = f"{user_input}\n\n[Calculation log for pk={pk}:\n{log}]"
        return self.llm.chat(PROMPT, augmented)

    def _extract_pk(self, text: str) -> int:
        match = re.search(r"\b(10\d{2})\b", text)
        return int(match.group(1)) if match else 1042