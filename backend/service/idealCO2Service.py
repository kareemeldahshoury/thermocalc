from backend.core.calculations.idealCO2 import IdealCO2Properties


def idealCO2Calculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    CO2 = IdealCO2Properties(inputs=inputs)
    result = CO2.calculate()
    return result