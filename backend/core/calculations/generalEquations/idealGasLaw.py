from typing import Dict

R = 8.314  # J/(mol·K)

def solve_ideal_gas_law(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}

    def validate_positive(vals: Dict[str, float]):
        for k, v in vals.items():
            if v <= 0:
                raise ValueError("All values must be > 0")

    if target == "P":
        vals = need("V", "T")
        n = inputs.get("n")
        m = inputs.get("m")
        M = inputs.get("M")

        if n is None:
            if m is None or M is None:
                raise ValueError("Need either n, or both m and M to solve for P")
            n = float(m) / float(M)

        validate_positive({"n": n, **vals})
        return (n * R * vals["T"]) / vals["V"]


    if target == "V":
        vals = need("P", "T")
        n = inputs.get("n")
        m = inputs.get("m")
        M = inputs.get("M")

        if n is None:
            if m is None or M is None:
                raise ValueError("Need either n, or both m and M to solve for V")
            n = float(m) / float(M)

        validate_positive({"n": n, **vals})
        return (n * R * vals["T"]) / vals["P"]


    if target == "T":
        vals = need("P", "V")
        n = inputs.get("n")
        m = inputs.get("m")
        M = inputs.get("M")

        if n is None:
            if m is None or M is None:
                raise ValueError("Need either n, or both m and M to solve for T")
            n = float(m) / float(M)

        validate_positive({"n": n, **vals})
        return (vals["P"] * vals["V"]) / (n * R)


    if target == "n":
        vals = need("P", "V", "T")
        validate_positive(vals)
        return (vals["P"] * vals["V"]) / (R * vals["T"])

 
    if target == "m":
        vals = need("P", "V", "T", "M")
        validate_positive(vals)
        n = (vals["P"] * vals["V"]) / (R * vals["T"])
        return n * vals["M"]


    if target == "M":
        vals = need("P", "V", "T", "m")
        validate_positive(vals)
        n = (vals["P"] * vals["V"]) / (R * vals["T"])
        if n == 0:
            raise ValueError("All values must be > 0")
        return vals["m"] / n

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'idealGasLaw'")
