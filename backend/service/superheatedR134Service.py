from backend.core.calculations.superheatedR134 import Superheat134aCalculation

def sh_134a(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    values = Superheat134aCalculation(inputs=inputs)
    result = values.calculate()
    return result