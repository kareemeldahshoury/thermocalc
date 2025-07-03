from backend.core.calculations.satR134T import Sat134aTCalculation
from backend.core.calculations.satR134P import Sat134aPCalculation

def sat_r134(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    if fluid_type in ["satR134T"]:
        sat134 = Sat134aTCalculation(inputs=inputs)
        result = sat134.calculate()
        return result
    else:
        sat134 = Sat134aPCalculation(inputs=inputs)
        result = sat134.calculate()
        return result
