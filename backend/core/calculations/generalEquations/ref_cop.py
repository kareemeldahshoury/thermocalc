from typing import Dict

def solve_ref_cop(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}

    if target == "COP":
        vals = need("Qc", "Qh")
        denom = vals["Qh"] - vals["Qc"]
        if denom == 0:
            raise ValueError("Qh - Qc cannot be zero.")
        cop = vals["Qc"] / denom
        if cop <= 0:
            raise ValueError(f"COP must be positive; computed COP={cop:.6g}. Check that Qh > Qc ≥ 0.")
        return cop

    if target == "Qc":
        vals = need("COP", "Qh")
        if vals["COP"] <= 0:
            raise ValueError("COP must be positive.")
        if (1 + vals["COP"]) == 0:
            raise ValueError("1 + COP cannot be zero.")
        return (vals["COP"] * vals["Qh"]) / (1 + vals["COP"])

    if target == "Qh":
        vals = need("COP", "Qc")
        if vals["COP"] <= 0:
            raise ValueError("COP must be positive.")
        return vals["Qc"] * (1 + vals["COP"]) / vals["COP"]

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'refEfficency'")
