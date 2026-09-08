MOCK_CALCULATIONS = [
    {
        "pk": 1040,
        "formula": "Si",
        "bandgap": 1.12,
        "state": "finished",
        "energy": -157.3,
    },
    {
        "pk": 1041,
        "formula": "GaN",
        "bandgap": 3.40,
        "state": "finished",
        "energy": -312.7,
    },
    {
        "pk": 1042,
        "formula": "TiO2",
        "bandgap": 3.05,
        "state": "failed",
        "energy": None,
    },
]

MOCK_LOGS = {
    1042: "ERROR: SCF convergence not reached after 50 iterations. Try increasing ecutwfc or smearing."
}


def submit_calculation(structure: str, parameters: dict) -> dict:
    return {
        "pk": 1043,
        "state": "submitted",
        "structure": structure,
        "parameters": parameters,
    }


def query_calculations(bandgap_gt: float = None) -> list:
    data = MOCK_CALCULATIONS

    if bandgap_gt is not None:
        data = [
            c for c in data
            if c.get("bandgap") is not None
            and c["bandgap"] > bandgap_gt
        ]

    return data


def get_calculation_log(pk: int) -> str:
    return MOCK_LOGS.get(
        pk,
        f"No errors found for pk={pk}. Calculation finished cleanly."
    )