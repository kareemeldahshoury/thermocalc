from typing import Dict

oh_data = {
    0: [0, 0, 0],
    298: [9188, 6709, 183.594],
    300: [9244, 6749, 183.779],
    500: [15181, 11024, 198.955],
    1000: [21809, 16219, 223.421],
    1500: [46046, 33575, 232.506],
    1700: [52706, 38571, 236.672],
    1800: [56089, 41123, 238.726],
    1900: [59905, 43708, 240.453],
    2000: [64256, 46323, 242.423],
    2050: [64687, 47462, 243.229],
    2100: [68196, 48688, 243.917],
    2150: [68177, 50361, 244.740],
    2200: [69392, 51641, 245.457],
    2250: [71694, 52987, 246.338],
    2300: [73462, 54339, 247.116],
    2350: [75236, 55967, 247.879],
    2400: [77015, 57061, 248.628],
    2450: [78801, 58431, 249.364],
    2500: [80592, 59796, 250.083],
    2550: [82388, 61186, 250.799],
    2600: [84189, 62591, 251.472],
    2650: [85995, 63962, 252.187],
    2700: [87792, 65323, 252.856],
    2750: [89622, 66757, 253.530],
    2800: [91463, 68161, 254.196],
    2850: [93266, 69570, 254.832],
    2900: [95094, 70976, 255.457],
    2950: [96936, 72378, 256.094],
    3000: [98763, 73786, 256.694],
    3050: [100622, 75181, 257.292],
    3100: [102447, 76586, 257.876],
    3200: [106145, 79539, 259.093],
    3300: [109855, 82418, 260.253],
    3400: [113578, 85309, 261.347],
    3500: [117312, 88212, 262.429],
}

def interpolate(val1, val2, x1, x2, x):
    return val1 + (val2 - val1) * (x - x1) / (x2 - x1)

class HydroxylOHProperties:
    def __init__(self, inputs: Dict[str, str]):
        self.inputs = inputs
        self.T = float(inputs.get("temperature", 0))
        self.temps = sorted(oh_data.keys())

    def calculate(self) -> Dict[str, float]:
        if not (self.temps[0] <= self.T <= self.temps[-1]):
            raise ValueError(f"Temperature {self.T} K out of range.")

        if self.T in oh_data:
            h, u, s = oh_data[self.T]
        else:
            for i in range(len(self.temps) - 1):
                T1, T2 = self.temps[i], self.temps[i + 1]
                if T1 <= self.T <= T2:
                    break
            v1 = oh_data[T1]
            v2 = oh_data[T2]

            h = interpolate(v1[0], v2[0], T1, T2, self.T)
            u = interpolate(v1[1], v2[1], T1, T2, self.T)
            s = interpolate(v1[2], v2[2], T1, T2, self.T)

        return {
            "temperature": self.T,
            "enthalpy (h)": round(h, 4),
            "internal_energy (u)": round(u, 4),
            "entropy (s°)": round(s, 5),
        }
