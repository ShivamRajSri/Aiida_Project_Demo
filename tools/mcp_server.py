from tools.mock_aiida import submit_calculation, query_calculations, get_calculation_log

# MCP-style tool registry: name -> {description, callable, schema}
TOOLS = {
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

def call_tool(name: str, **kwargs):
    if name not in TOOLS:
        raise ValueError(f"Unknown tool: {name}")
    return TOOLS[name]["fn"](**kwargs)

def list_tools() -> str:
    return "\n".join(f"- {k}: {v['description']}" for k, v in TOOLS.items())
```

---

### 6. `rag/` — Knowledge base + retriever

**`rag/knowledge_base/aiida_basics.txt`**
```
AiiDA is a Python framework for managing computational workflows.
Each simulation is stored as a node in a directed acyclic graph (provenance graph).
Calculations are identified by their primary key (pk).
WorkChains are AiiDA's way of defining multi-step workflows.
```

**`rag/knowledge_base/qe_inputs.txt`**
```
Quantum ESPRESSO geometry optimization uses the relax or vc-relax calculation type.
ecutwfc controls the plane-wave cutoff energy; typical values are 40-80 Ry.
SCF convergence failures often require increasing ecutwfc, smearing, or k-points.
The pw.x code handles DFT calculations in Quantum ESPRESSO.