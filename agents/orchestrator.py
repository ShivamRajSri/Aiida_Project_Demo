from pathlib import Path
from llm.model_client import ModelClient
from agents.workflow_agent   import WorkflowAgent
from agents.analysis_agent   import AnalysisAgent
from agents.diagnostic_agent import DiagnosticAgent

PROMPT = Path("config/prompts/orchestrator.txt").read_text()

class Orchestrator:
    def __init__(self):
        self.llm        = ModelClient()
        self.agents     = {
            "WORKFLOW":   WorkflowAgent(),
            "ANALYSIS":   AnalysisAgent(),
            "DIAGNOSTIC": DiagnosticAgent(),
        }

    def handle(self, user_input: str) -> str:
        route = self.llm.chat(PROMPT, user_input).strip().upper()
        agent = self.agents.get(route)
        if agent:
            return agent.handle(user_input)
        return "I'm not sure how to help with that. Try asking about running, querying, or diagnosing a calculation."