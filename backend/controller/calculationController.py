from backend.service.satWaterService import sat_water
from backend.service.superHeatedWaterService import sh_water
from backend.service.idealAirService import idealAirCalculation
from backend.service.idealN2Service import idealN2Calculation



# Handles the variables to send to the proper calculation file
def handle_calculation_satwater(fluid_type: str, substance: str, inputs: dict):
    if "satWater" in fluid_type:
        result = sat_water(fluid_type, inputs)
        return result
    else:
        return "Calculation not implemented yet."
    
def handle_calculation_superHeatedWater(fluid_type: str, substance: str, inputs: dict):
    result = sh_water(fluid_type, inputs)
    return result
    
def handle_calculation_idealAir(fluid_type: str, substance: str, inputs: dict):
    result = idealAirCalculation(fluid_type, inputs)
    return result

def handle_calculation_N2(fluid_type: str, substance: str, inputs: dict):
    result = idealN2Calculation(fluid_type, inputs)
    return result