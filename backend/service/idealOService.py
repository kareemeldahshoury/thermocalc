from backend.core.calculations.idealO import MonatomicOxygenProperties

def idealOCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    O = MonatomicOxygenProperties(inputs=inputs)
    result = O.calculate()
    return result