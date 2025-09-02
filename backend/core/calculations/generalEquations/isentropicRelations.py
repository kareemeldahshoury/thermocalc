from typing import Dict
import math

def solve_isentropic_relations(solve_for: str, inputs: Dict[str, float]) -> float:
    target = (solve_for or "").strip()

    def need(*keys: str) -> Dict[str, float]:
        missing = [k for k in keys if inputs.get(k) is None]
        if missing:
            raise ValueError(f"Missing inputs: {', '.join(missing)}")
        return {k: float(inputs[k]) for k in keys}

    def validate_positive(vals: Dict[str, float]):
        for k, v in vals.items():
            if v <= 0:
                raise ValueError(f"All values must be > 0, got {k}={v}")

    if target == "T2":
        if "P1" in inputs and "P2" in inputs:
            vals = need("T1", "P1", "P2", "gamma")
            validate_positive(vals)
            return vals["T1"] * (vals["P2"]/vals["P1"])**((vals["gamma"]-1)/vals["gamma"])
        
        elif "V1" in inputs and "V2" in inputs:
            vals = need("T1", "V1", "V2", "gamma")
            validate_positive(vals)
            return vals["T1"] * (vals["V1"]/vals["V2"])**(vals["gamma"]-1)
        else:
            raise ValueError("Need either (P1,P2) or (V1,V2) to solve for T2")

    if target == "T1":
        if "P1" in inputs and "P2" in inputs:
            vals = need("T2", "P1", "P2", "gamma")
            validate_positive(vals)
            return vals["T2"] / ((vals["P2"]/vals["P1"])**((vals["gamma"]-1)/vals["gamma"]))
        
        elif "V1" in inputs and "V2" in inputs:
            vals = need("T2", "V1", "V2", "gamma")
            validate_positive(vals)
            return vals["T2"] / ((vals["V1"]/vals["V2"])**(vals["gamma"]-1))
        else:
            raise ValueError("Need either (P1,P2) or (V1,V2) to solve for T1")

    if target == "P2":
        if "T1" in inputs and "T2" in inputs:
            vals = need("P1", "T1", "T2", "gamma")
            validate_positive(vals)
            return vals["P1"] * (vals["T2"]/vals["T1"])**(vals["gamma"]/(vals["gamma"]-1))
        
        elif "V1" in inputs and "V2" in inputs:
            vals = need("P1", "V1", "V2", "gamma")
            validate_positive(vals)
            return vals["P1"] * (vals["V1"]/vals["V2"])**(vals["gamma"])
        else:
            raise ValueError("Need either (T1,T2) or (V1,V2) to solve for P2")

    if target == "P1":
        if "T1" in inputs and "T2" in inputs:
            vals = need("P2", "T1", "T2", "gamma")
            validate_positive(vals)
            return vals["P2"] / ((vals["T2"]/vals["T1"])**(vals["gamma"]/(vals["gamma"]-1)))
        
        elif "V1" in inputs and "V2" in inputs:
            vals = need("P2", "V1", "V2", "gamma")
            validate_positive(vals)
            return vals["P2"] / ((vals["V1"]/vals["V2"])**(vals["gamma"]))
        else:
            raise ValueError("Need either (T1,T2) or (V1,V2) to solve for P1")

    if target == "V2":
        if "T1" in inputs and "T2" in inputs:
            vals = need("V1", "T1", "T2", "gamma")
            validate_positive(vals)
            return vals["V1"] * (vals["T1"]/vals["T2"])**(1/(vals["gamma"]-1))
        
        elif "P1" in inputs and "P2" in inputs:
            vals = need("V1", "P1", "P2", "gamma")
            validate_positive(vals)
            return vals["V1"] * (vals["P1"]/vals["P2"])**(1/vals["gamma"])
        else:
            raise ValueError("Need either (T1,T2) or (P1,P2) to solve for V2")

    if target == "V1":
        if "T1" in inputs and "T2" in inputs:
            vals = need("V2", "T1", "T2", "gamma")
            validate_positive(vals)
            return vals["V2"] * (vals["T2"]/vals["T1"])**(1/(vals["gamma"]-1))
        
        elif "P1" in inputs and "P2" in inputs:
            vals = need("V2", "P1", "P2", "gamma")
            validate_positive(vals)
            return vals["V2"] * (vals["P2"]/vals["P1"])**(1/vals["gamma"])
        else:
            raise ValueError("Need either (T1,T2) or (P1,P2) to solve for V1")

    if target == "gamma":

        if all(k in inputs for k in ["T1","T2","P1","P2"]):
            vals = need("T1","T2","P1","P2")
            validate_positive(vals)
            ratio = math.log(vals["T2"]/vals["T1"]) / math.log(vals["P2"]/vals["P1"])
            return 1 / (1 - ratio)
        
        if all(k in inputs for k in ["P1","P2","V1","V2"]):
            vals = need("P1","P2","V1","V2")
            validate_positive(vals)
            ratio = math.log(vals["P2"]/vals["P1"]) / math.log(vals["V1"]/vals["V2"])
            return ratio
        
        if all(k in inputs for k in ["T1","T2","V1","V2"]):
            vals = need("T1","T2","V1","V2")
            validate_positive(vals)
            ratio = math.log(vals["T2"]/vals["T1"]) / math.log(vals["V1"]/vals["V2"])
            return 1 + ratio
        raise ValueError("To solve for gamma, provide either (T1,T2,P1,P2), (P1,P2,V1,V2), or (T1,T2,V1,V2)")

    raise ValueError(f"Unknown solveFor '{solve_for}' for 'isentropicRelations'")
