from backend.core.calculations.idealCOcalc import IdealCOProperties


def idealCOCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    CO = IdealCOProperties(inputs=inputs)
    result = CO.calculate()
    return result