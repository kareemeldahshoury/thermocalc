from backend.core.calculations.idealH2 import IdealHydrogenProperties


def idealH2Calculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    H2 = IdealHydrogenProperties(inputs=inputs)
    result = H2.calculate()
    return result