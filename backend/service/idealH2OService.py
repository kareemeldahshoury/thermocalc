from backend.core.calculations.idealH2Ocalc import IdealWaterProperties


def idealH2OCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    H2O = IdealWaterProperties(inputs=inputs)
    result = H2O.calculate()
    return result