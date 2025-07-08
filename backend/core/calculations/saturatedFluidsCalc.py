from typing import Dict
from backend.core.calculations.saturatedFluidsData import sat_dic

def interpolate(value1, value2, x1, x2, x):
    return value1 + (value2 - value1) * (x - x1) / (x2 - x1)


class SaturatedFluidCalculation:
    def __init__(self, fluid_type: str, inputs: Dict[str, str]):
        self.fluid_type = fluid_type
        self.inputs = inputs
        self.table = sat_dic.get(fluid_type)
        if not self.table:
            raise ValueError(f"No saturation data found for fluid type '{fluid_type}'")

        self.keys_sorted = sorted(self.table.keys())
        self.lookup_type = "temperature" if "temperature" in inputs else "pressure"
        self.x_value = float(inputs.get("quality", 0))
        self.lookup_value = float(inputs.get(self.lookup_type, 0))

    def calculate(self) -> Dict[str, float]:
        if not (self.keys_sorted[0] <= self.lookup_value <= self.keys_sorted[-1]):
            raise ValueError(f"{self.lookup_type.title()} {self.lookup_value} not in range.")
        if not (0 <= self.x_value <= 1):
            raise ValueError(f"Quality {self.x_value} must be between 0 and 1.")

        # Direct match
        if self.lookup_value in self.table:
            props = self.table[self.lookup_value]
        else:
            # Interpolate between bounds
            for i in range(len(self.keys_sorted) - 1):
                low, high = self.keys_sorted[i], self.keys_sorted[i + 1]
                if low <= self.lookup_value <= high:
                    break
            props_low = self.table[low]
            props_high = self.table[high]

            props = [
                interpolate(props_low[j], props_high[j], low, high, self.lookup_value)
                for j in range(len(props_low))
            ]

        # Unpack interpolated or matched values
        temp_sat, vf, vg, uf, ufg, _, hf, hfg, _, sf, sfg, _ = props

        v = vf + self.x_value * (vg - vf)
        u = uf + self.x_value * ufg
        h = hf + self.x_value * hfg
        s = sf + self.x_value * sfg

        return {
            "fluid_type": self.fluid_type,
            self.lookup_type: self.lookup_value,
            "quality": self.x_value,
            "saturation_temperature": round(temp_sat, 2),
            "specific_volume": round(v, 6),
            "internal_energy": round(u, 2),
            "enthalpy": round(h, 2),
            "entropy": round(s, 4),
        }