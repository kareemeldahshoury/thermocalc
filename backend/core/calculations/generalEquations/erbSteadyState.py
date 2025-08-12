from typing import Dict
import math

def solve_erb_steady_state(solve_for: str, inputs: Dict[str, float]) -> float:
    sf = (solve_for or "").strip()

    def need(*names: str) -> Dict[str, float]:
        missing = [n for n in names if inputs.get(n) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        out: Dict[str, float] = {}
        for n in names:
            try:
                out[n] = float(inputs[n])
            except Exception:
                raise ValueError(f"'{n}' must be a number")
        return out

    def opt(name: str):
        v = inputs.get(name)
        return float(v) if v is not None else None

    def delta_terms(h1: float, h2: float, V1: float, V2: float,
                    z1: float | None, z2: float | None, g: float) -> float:
        """Return Δh + Δke [+ Δpe if z1/z2 given], in kJ/kg."""
        dh  = h1 - h2                              # kJ/kg
        dke = (V1**2 - V2**2) / 2000.0             # kJ/kg  (since J/kg / 1000)
        dpe = g * (z1 - z2) / 1000.0 if (z1 is not None and z2 is not None) else 0.0
        return dh + dke + dpe

    # Optional potential inputs
    z1 = opt("z1")
    z2 = opt("z2")
    g  = float(inputs.get("g", 9.81))

    if sf == "Qdot":
        vals = need("Wdot", "mdot", "h1", "h2", "V1", "V2")
        rhs = delta_terms(vals["h1"], vals["h2"], vals["V1"], vals["V2"], z1, z2, g)
        return vals["Wdot"] - vals["mdot"] * rhs

    elif sf == "Wdot":
        vals = need("Qdot", "mdot", "h1", "h2", "V1", "V2")
        rhs = delta_terms(vals["h1"], vals["h2"], vals["V1"], vals["V2"], z1, z2, g)
        return vals["Qdot"] + vals["mdot"] * rhs

    elif sf == "mdot":
        vals = need("Qdot", "Wdot", "h1", "h2", "V1", "V2")
        rhs = delta_terms(vals["h1"], vals["h2"], vals["V1"], vals["V2"], z1, z2, g)
        if rhs == 0:
            raise ValueError("Denominator is zero (Δh + Δke [+Δpe]) = 0; cannot solve for mdot.")
        return (vals["Wdot"] - vals["Qdot"]) / rhs

    elif sf == "h1":
        vals = need("Qdot", "Wdot", "mdot", "h2", "V1", "V2")
        dke = (vals["V1"]**2 - vals["V2"]**2) / 2000.0
        dpe = g * (z1 - z2) / 1000.0 if (z1 is not None and z2 is not None) else 0.0
        return vals["h2"] - (dke + dpe) + (vals["Wdot"] - vals["Qdot"]) / vals["mdot"]

    elif sf == "h2":
        vals = need("Qdot", "Wdot", "mdot", "h1", "V1", "V2")
        dke = (vals["V1"]**2 - vals["V2"]**2) / 2000.0
        dpe = g * (z1 - z2) / 1000.0 if (z1 is not None and z2 is not None) else 0.0
        return vals["h1"] + (dke + dpe) - (vals["Wdot"] - vals["Qdot"]) / vals["mdot"]

    elif sf == "V1":
        vals = need("Qdot", "Wdot", "mdot", "h1", "h2", "V2")
        rhs = (vals["Wdot"] - vals["Qdot"]) / vals["mdot"] - (vals["h1"] - vals["h2"])
        rhs -= (g * (z1 - z2) / 1000.0) if (z1 is not None and z2 is not None) else 0.0
        V1_sq = vals["V2"]**2 + 2000.0 * rhs
        if V1_sq < 0:
            raise ValueError("Computed V1^2 is negative; check inputs.")
        return math.sqrt(V1_sq)

    elif sf == "V2":
        vals = need("Qdot", "Wdot", "mdot", "h1", "h2", "V1")
        rhs = (vals["Wdot"] - vals["Qdot"]) / vals["mdot"] - (vals["h1"] - vals["h2"])
        rhs -= (g * (z1 - z2) / 1000.0) if (z1 is not None and z2 is not None) else 0.0
        V2_sq = vals["V1"]**2 - 2000.0 * rhs
        if V2_sq < 0:
            raise ValueError("Computed V2^2 is negative; check inputs.")
        return math.sqrt(V2_sq)

    else:
        raise ValueError(f"Unknown solveFor '{solve_for}' for 'erb1SteadyState'")
