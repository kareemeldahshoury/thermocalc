from backend.core.calculations.sat_water_p import SatWaterPCalculation

def handle_calculation(fluid_type: str, substance: str, inputs: dict):
    if fluid_type == "satWaterP":
        calc = SatWaterPCalculation(substance, inputs)
        return calc.calculate()
    else:
        return "Calculation not implemented yet."