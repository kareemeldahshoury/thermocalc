from math import log
from typing import Dict

R = 8.314  # J/mol·K

def calculate_work(process: str, inputs: Dict[str, float]) -> Dict[str, float]:
    """
    Returns a dictionary with labeled and formatted result,
    raises ValueError on bad input
    """
    if process == "isobaric":
        P = inputs["P"]
        V1 = inputs["V1"]
        V2 = inputs["V2"]
        work = P * (V2 - V1)

    elif process == "isothermal":
        V1 = inputs["V1"]
        V2 = inputs["V2"]
        T = inputs["T"]
        n = inputs["n"]
        work = n * R * T * log(V2 / V1)

    elif process == "adiabatic":
        P1 = inputs["P1"]
        V1 = inputs["V1"]
        V2 = inputs["V2"]
        gamma = inputs["gamma"]
        work = (P1 * V1 - P1 * (V1 * (V1 / V2) ** (gamma - 1))) / (gamma - 1)

    elif process == "polytropic":
        P1 = inputs["P1"]
        V1 = inputs["V1"]
        V2 = inputs["V2"]
        n = inputs["n"]

        if n == 1:
            T = inputs["T"]
            work = R * T * log(V2 / V1)
        else:
            P2 = inputs.get("P2")
            if P2 is not None:
                work = (P2 * V2 - P1 * V1) / (1 - n)
            else:
                work = (P1 * V1) * ((1 - (V1 / V2) ** (n - 1)) / (n - 1))

    else:
        raise ValueError(f"Unsupported process: {process}")

    return {
        "Work<br>(W, J)": round(work, 4)
    }
