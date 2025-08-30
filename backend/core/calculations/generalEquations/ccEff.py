from typing import Dict

def solve_carnot_efficiency(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}

    if target == "ccEff":
        vals = need("TH", "TL")
        if vals["TH"] <= 0 or vals["TL"] <= 0:
            raise ValueError("Temperatures must be positive.")
        if vals["TL"] >= vals["TH"]:
            raise ValueError("T<sub>L</sub> must be less than T<sub>H</sub>.")
        return 1 - vals["TL"] / vals["TH"]

    if target == "TH":
        vals = need("ccEff", "TL")
        if not (0 <= vals["ccEff"] < 1):
            raise ValueError(f"η must be between 0 and 1")
        if vals["TL"] <= 0:
            raise ValueError("Temperatures must be positive.")
        return vals["TL"] / (1 - vals["ccEff"])

    if target == "TL":
        vals = need("ccEff", "TH")
        if not (0 <= vals["ccEff"] < 1):
            raise ValueError(f"η must be between 0 and 1")
        if vals["TH"] <= 0:
            raise ValueError("Temperatures must be positive.")
        return vals["TH"] * (1 - vals["ccEff"])

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'carnotEfficiency'")
