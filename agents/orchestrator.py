from pathlib import Path

from llm.model_client import ModelClient
from agents.workflow_agent import WorkflowAgent
from agents.analysis_agent import AnalysisAgent
from agents.diagnostic_agent import DiagnosticAgent
from agents.general_agent import GeneralAgent


PROMPT = Path(
    "config/prompts/orchestrator.txt"
).read_text()


class Orchestrator:
    def __init__(self):
        self.llm = ModelClient()

        self.agents = {
            "WORKFLOW": WorkflowAgent(),
            "ANALYSIS": AnalysisAgent(),
            "DIAGNOSTIC": DiagnosticAgent(),
            "GENERAL": GeneralAgent(),
        }

    def handle(self, user_input: str) -> str:
        route = self.llm.chat(
            PROMPT,
            user_input
        ).strip().upper()

        # Handle accidental extra text from the LLM
        if route not in self.agents:
            for label in self.agents:
                if label in route:
                    route = label
                    break

        agent = self.agents.get(route)

        if agent:
            return agent.handle(user_input)

        return (
            "I couldn't determine what you want to do. "
            "Please ask about AiiDA workflows, calculation results, "
            "calculation errors, or general AiiDA concepts."
        )