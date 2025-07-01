from backend.core.calculations.satR134T import Sat134aTCalculation

def sat_r134(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    if fluid_type == "satR134T":
        sat134 = Sat134aTCalculation(inputs=inputs)
        result = sat134.calculate()
        return result
    # else:
    #     satWaterT = SatWaterTCalculation(inputs=inputs)
    #     result = satWaterT.calculate()
    #     return result