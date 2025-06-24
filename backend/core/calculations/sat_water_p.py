from typing import Dict

P_sat = {
    0.01: [6.97, 0.001000, 129.19, 29.302, 2355.2, 2384.5, 29.303, 2484.4, 2513.7, 0.1059, 8.8690, 8.9749],
    0.15: [13.02, 0.001001, 87.964, 54.686, 2338.1, 2392.8, 54.688, 2470.1, 2524.7, 0.1956, 8.6314, 8.8270],
    0.20: [17.50, 0.001001, 66.990, 73.431, 2325.5, 2398.9, 73.433, 2459.5, 2532.9, 0.2606, 8.4621, 8.7227],
    
}

def interpolate(value1, value2, x1, x2, x):
    return value1 + (value2 - value1) * (x - x1) / (x2 - x1)

class SatWaterPCalculation:
    def __init__(self, substance: str, inputs: Dict[str, str]):
        self.inputs = inputs
        self.pressure = float(inputs.get("pressure", 0))
        self.x_value = float(inputs.get("quality", 0))
        self.pressures = sorted(P_sat.keys())

    def calculate(self) -> str:
        if not (self.pressures[0] <= self.pressure <= self.pressures[-1]):
            raise ValueError(f"Pressure {self.pressure} bar not available in table range.")
        if not (0 <= self.x_value <= 1):
            raise ValueError(f"Quality {self.x_value} must be between 0 and 1.")

        if self.pressure in P_sat:
            props = P_sat[self.pressure]
            temp_sat, vf, vg, uf, ufg, _, hf, hfg, _, sf, sfg, _ = props
        else:
            for i in range(len(self.pressures) - 1):
                if self.pressures[i] <= self.pressure <= self.pressures[i+1]:
                    p_low, p_high = self.pressures[i], self.pressures[i+1]
                    break
            props_low = P_sat[p_low]
            props_high = P_sat[p_high]

            temp_sat = interpolate(props_low[0], props_high[0], p_low, p_high, self.pressure)
            vf = interpolate(props_low[1], props_high[1], p_low, p_high, self.pressure)
            vg = interpolate(props_low[2], props_high[2], p_low, p_high, self.pressure)
            uf = interpolate(props_low[3], props_high[3], p_low, p_high, self.pressure)
            ufg = interpolate(props_low[4], props_high[4], p_low, p_high, self.pressure)
            hf = interpolate(props_low[6], props_high[6], p_low, p_high, self.pressure)
            hfg = interpolate(props_low[7], props_high[7], p_low, p_high, self.pressure)
            sf = interpolate(props_low[9], props_high[9], p_low, p_high, self.pressure)
            sfg = interpolate(props_low[10], props_high[10], p_low, p_high, self.pressure)

        v = vf + self.x_value * (vg - vf)
        u = uf + self.x_value * ufg
        h = hf + self.x_value * hfg
        s = sf + self.x_value * sfg

        return (
            f"At {self.pressure} bar and quality {self.x_value}:\n"
            f"Saturation Temp = {temp_sat:.2f} °C\n"
            f"Specific Volume (v) = {v:.6f} m³/kg\n"
            f"Internal Energy (u) = {u:.2f} kJ/kg\n"
            f"Enthalpy (h) = {h:.2f} kJ/kg\n"
            f"Entropy (s) = {s:.4f} kJ/kg·K"
        )
