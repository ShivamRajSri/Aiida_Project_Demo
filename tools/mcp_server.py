from typing import Any, Callable

from tools.mock_aiida import (
    submit_calculation,
    query_calculations,
    get_calculation_log,
)


TOOLS: dict[str, dict[str, Any]] = {
    "submit_calculation": {
        "description": "Submit a new AiiDA calculation for a given structure.",
        "fn": submit_calculation,
        "params": ["structure", "parameters"],
    },
    "query_calculations": {
        "description": "Query finished calculations, optionally filtering by bandgap.",
        "fn": query_calculations,
        "params": ["bandgap_gt"],
    },
    "get_calculation_log": {
        "description": "Retrieve the error log for a calculation by its PK.",
        "fn": get_calculation_log,
        "params": ["pk"],
    },
}


def call_tool(name: str, **kwargs: Any) -> Any:
    if name not in TOOLS:
        raise ValueError(f"Unknown tool: {name}")

    tool = TOOLS[name]
    fn: Callable[..., Any] = tool["fn"]

    return fn(**kwargs)


def list_tools() -> str:
    return "\n".join(
        f"- {name}: {tool['description']}"
        for name, tool in TOOLS.items()
    )