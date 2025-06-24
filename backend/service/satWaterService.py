from backend.core.calculations.satWaterP import SatWaterPCalculation

# calculation_registry = {
#     "satWaterP": SatWaterPCalculation,
#     # others...
# }


def sat_water(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    if fluid_type == "satWaterP":
        satWaterP = SatWaterPCalculation(inputs=inputs)
        result = satWaterP.calculate()
        return result
