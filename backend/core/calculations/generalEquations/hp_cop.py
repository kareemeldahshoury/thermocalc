from typing import Dict

def solve_hp_cop(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}


    if target == "COP":
        if "Wnet" in inputs and inputs["Wnet"] is not None:
            vals = need("Qh", "Wnet")
            if vals["Wnet"] == 0:
                raise ValueError("W<sub>net</sub> cannot be zero")
            if vals["Qh"] <= 0:
                raise ValueError("Q<sub>h</sub> must be greater than 0")
            cop = vals["Qh"] / vals["Wnet"]
            if cop <= 0:
                raise ValueError(f"COP must be positive; computed COP={cop:.4g}")
            return cop
        else:
            vals = need("Qh", "Qc")
            if vals["Qh"] <= 0 or vals["Qc"] <= 0:
                raise ValueError("Q<sub>h</sub> and Q<sub>c</sub> must be greater than 0")
            denom = vals["Qh"] - vals["Qc"]
            if denom == 0:
                raise ValueError("Q<sub>h</sub> - Q<sub>c</sub> cannot be zero")
            cop = vals["Qh"] / denom
            if cop <= 0:
                raise ValueError(
                    f"COP must be positive; computed COP={cop:.6g}. "
                )
            return cop


    if target == "Qh":
        if "Wnet" in inputs and inputs["Wnet"] is not None:
            vals = need("COP", "Wnet")
            if vals["COP"] <= 0:
                raise ValueError("COP must be positive")
            return vals["COP"] * vals["Wnet"]
        else:
            vals = need("COP", "Qc")
            if vals["COP"] <= 0:
                raise ValueError("COP must be positive")
            if vals["Qc"] <= 0:
                raise ValueError("Q<sub>c</sub> must be greater than 0")
            return (vals["COP"] * vals["Qc"]) / (vals["COP"] - 1)


    if target == "Wnet":
        vals = need("COP", "Qh")
        if vals["COP"] <= 1:
            raise ValueError("COP must be > 1 for a heat pump.")
        if vals["Qh"] <= 0:
            raise ValueError("Q<sub>h</sub> must be greater than 0")
        return vals["Qh"] / vals["COP"]

    if target == "Qc":
        vals = need("Qh", "COP")
        if vals["COP"] <= 1:
            raise ValueError("COP must be > 1 for a heat pump.")
        if vals["Qh"] <= 0:
            raise ValueError("Q<sub>h</sub> must be greater than 0")
        return vals["Qh"] * (1 - 1 / vals["COP"])

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'heatPumpEfficiency'")
