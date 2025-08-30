from typing import Dict

def solve_mass_flow_rate(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}


    if target == "mdot":
        vals = need("V", "A", "v")
        if vals["v"] <= 0:
            raise ValueError("Specific volume must be > 0")
        if vals["A"] <= 0:
            raise ValueError("Area must be > 0")
        if vals["V"] == 0:
            raise ValueError("Velocity must be > 0")
        return vals["V"] * vals["A"] / vals["v"]


    if target == "V":
        vals = need("mdot", "A", "v")
        if vals["A"] <= 0:
            raise ValueError("Area must be > 0")
        if vals["v"] <= 0:
            raise ValueError("Specific volume must be > 0")
        if vals["mdot"] <= 0:
            raise ValueError("Mass flow rate must be > 0")
        return vals["mdot"] * vals["v"] / vals["A"]


    if target == "A":
        vals = need("mdot", "V", "v")
        if vals["V"] == 0:
            raise ValueError("Velocity must be > 0")
        if vals["mdot"] <= 0:
            raise ValueError("Mass flow rate must be > 0")
        if vals["v"] <= 0:
            raise ValueError("Specific volume must be > 0")
        return vals["mdot"] * vals["v"] / vals["V"]

    if target == "v":
        vals = need("mdot", "V", "A")
        if vals["mdot"] <= 0:
            raise ValueError("Mass flow rate must be > 0")
        if vals["V"] == 0:
            raise ValueError("Velocity must be > 0")
        if vals["A"] <= 0:
            raise ValueError("Area must be > 0")
        return vals["V"] * vals["A"] / vals["mdot"]

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'massFlowRate'")
