from backend.core.calculations.satIceWat import SatIceWaterCalculation

def satIceWatCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    values = SatIceWaterCalculation(inputs=inputs)
    result = values.calculate()
    return result