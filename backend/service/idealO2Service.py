from backend.core.calculations.idealO2 import IdealOxygenProperties

def idealO2Calculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    O2 = IdealOxygenProperties(inputs=inputs)
    result = O2.calculate()
    return result