from backend.core.calculations.idealN2 import IdealNitrogenProperties

def idealN2Calculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    N2 = IdealNitrogenProperties(inputs=inputs)
    result = N2.calculate()
    return result