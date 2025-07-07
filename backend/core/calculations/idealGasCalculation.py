from typing import Dict
from backend.core.calculations.idealGasTables import gas_tables

def interpolate(val1, val2, x1, x2, x):
    return val1 + (val2 - val1) * (x - x1) / (x2 - x1)

class IdealGasProperties:
    def __init__(self, substance: str, inputs: Dict[str, str]):
        self.T = float(inputs.get("temperature", 0))
        self.data = gas_tables.get(substance.lower())
        if not self.data:
            raise ValueError(f"Gas '{substance}' not found.")
        self.temps = sorted(self.data.keys())

    def calculate(self) -> Dict[str, float]:
        if not (self.temps[0] <= self.T <= self.temps[-1]):
            raise ValueError(f"Temperature {self.T} K out of range.")

        if self.T in self.data:
            h, u, s = self.data[self.T]
        else:
            for i in range(len(self.temps) - 1):
                T1, T2 = self.temps[i], self.temps[i + 1]
                if T1 <= self.T <= T2:
                    break
            v1 = self.data[T1]
            v2 = self.data[T2]
            h = interpolate(v1[0], v2[0], T1, T2, self.T)
            u = interpolate(v1[1], v2[1], T1, T2, self.T)
            s = interpolate(v1[2], v2[2], T1, T2, self.T)

        return {
            "temperature (K)": self.T,
            "enthalpy (h) [kJ/kg]": round(h, 4),
            "internal energy (u) [kJ/kg]": round(u, 4),
            "entropy (s°) [kJ/kg·K]": round(s, 5),
        }
