from backend.core.calculations.idealAir import IdealAirProperties

def idealAirCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    air = IdealAirProperties(inputs=inputs)
    result = air.calculate()
    return result