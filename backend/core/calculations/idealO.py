from typing import Dict

mono_oxygen_data = {
    0: [0, 0, 0],
    298: [6852, 4373, 160.944],
    300: [6892, 4398, 161.079],
    500: [11197, 7040, 172.088],
    1000: [21713, 13938, 186.672],
    1500: [32150, 19679, 195.143],
    1700: [36317, 22183, 197.751],
    1800: [38422, 23496, 199.132],
    1900: [40482, 24865, 200.067],
    2000: [42564, 25694, 200.597],
    2050: [43605, 26560, 201.649],
    2100: [44646, 26718, 202.151],
    2150: [45687, 27811, 202.641],
    2200: [46728, 28436, 203.119],
    2250: [47769, 29262, 203.588],
    2300: [48811, 29688, 204.045],
    2350: [49852, 30314, 204.493],
    2400: [50894, 30940, 204.932],
    2450: [51936, 31566, 205.362],
    2500: [52979, 32193, 205.783],
    2550: [54021, 32820, 206.196],
    2600: [55063, 33447, 206.600],
    2650: [56108, 34075, 206.999],
    2700: [57154, 34704, 207.390],
    2750: [58196, 35332, 207.772],
    2800: [59243, 35961, 208.148],
    2850: [60286, 36590, 208.518],
    2900: [61332, 37220, 208.882],
    2950: [62378, 37851, 209.242],
    3000: [63425, 38482, 209.592],
    3050: [64523, 39096, 210.029],
    3100: [65619, 39710, 210.453],
    3200: [67619, 41013, 210.934],
    3300: [69724, 42323, 211.655],
    3400: [71821, 43630, 212.220],
    3500: [73932, 44832, 212.831],
}

def interpolate(val1, val2, x1, x2, x):
    return val1 + (val2 - val1) * (x - x1) / (x2 - x1)

class MonatomicOxygenProperties:
    def __init__(self, inputs: Dict[str, str]):
        self.inputs = inputs
        self.T = float(inputs.get("temperature", 0))
        self.temps = sorted(mono_oxygen_data.keys())

    def calculate(self) -> Dict[str, float]:
        if not (self.temps[0] <= self.T <= self.temps[-1]):
            raise ValueError(f"Temperature {self.T} K out of range.")

        if self.T in mono_oxygen_data:
            h, u, s = mono_oxygen_data[self.T]
        else:
            for i in range(len(self.temps) - 1):
                T1, T2 = self.temps[i], self.temps[i + 1]
                if T1 <= self.T <= T2:
                    break
            v1 = mono_oxygen_data[T1]
            v2 = mono_oxygen_data[T2]

            h = interpolate(v1[0], v2[0], T1, T2, self.T)
            u = interpolate(v1[1], v2[1], T1, T2, self.T)
            s = interpolate(v1[2], v2[2], T1, T2, self.T)

        return {
            "temperature": self.T,
            "enthalpy (h)": round(h, 4),
            "internal_energy (u)": round(u, 4),
            "entropy (s°)": round(s, 5),
        }
