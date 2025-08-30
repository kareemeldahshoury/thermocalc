from typing import Dict

def solve_ref_cop(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}


    if target == "COP":
        if "Wnet" in inputs and inputs["Wnet"] is not None:
            vals = need("Qc", "Wnet")
            if vals["Wnet"] == 0:
                raise ValueError("Wnet cannot be zero")
            cop = vals["Qc"] / vals["Wnet"]
            if cop <= 0:
                raise ValueError(f"COP must be positive; computed COP={cop:.4g}")
            return cop
        else:
            vals = need("Qc", "Qh")
            denom = vals["Qh"] - vals["Qc"]
            if denom == 0:
                raise ValueError("Qh - Qc cannot be zero")
            cop = vals["Qc"] / denom
            if cop <= 0:
                raise ValueError(f"COP must be positive; computed COP={cop:.6g}. Check that Qh > Qc ≥ 0")
            return cop


    if target == "Qc":
        if "Wnet" in inputs and inputs["Wnet"] is not None:
            vals = need("COP", "Wnet")
            if vals["COP"] <= 0:
                raise ValueError("COP must be positive")
            return vals["COP"] * vals["Wnet"]
        else:
            vals = need("COP", "Qh")
            if vals["COP"] <= 0:
                raise ValueError("COP must be positive")
            return (vals["COP"] * vals["Qh"]) / (1 + vals["COP"])


    if target == "Qh":
        vals = need("COP", "Qc")
        if vals["COP"] <= 0:
            raise ValueError("COP must be positive.")
        return vals["Qc"] * (1 + vals["COP"]) / vals["COP"]


    if target == "Wnet":
        if "Qc" in inputs and "COP" in inputs and inputs["COP"] is not None:
            vals = need("COP", "Qc")
            if vals["COP"] <= 0:
                raise ValueError("COP must be positive.")
            return vals["Qc"] / vals["COP"]
        elif "Qh" in inputs and "Qc" in inputs:
            vals = need("Qh", "Qc")
            return vals["Qh"] - vals["Qc"]
        else:
            raise ValueError("Need either (COP, Qc) or (Qh, Qc) to solve for Wnet")

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'refEfficency'")
