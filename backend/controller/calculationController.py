from backend.service.satWaterService import sat_water
from backend.service.superHeatedWaterService import sh_water
from backend.service.idealAirService import idealAirCalculation
from backend.service.satR134Service import sat_r134
from backend.service.satIceWatService import satIceWatCalculation
from backend.service.superheatedR134Service import sh_134a
from backend.core.calculations.molGCP import molGCPCalculation
from backend.core.calculations.specHeat300 import idealGas300KCalculation
from backend.core.calculations.specHeat import specHeatCalculation
from backend.core.calculations.idealGasCalculation import IdealGasProperties

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

def handle_calculation_satR134(fluid_type: str, substance: str, inputs: dict):
    if "satR134" in fluid_type:
        result = sat_r134(fluid_type, inputs)
        return result
    else:
        return "Calculation not implemented yet."
    
def handle_calculation_satIceWat(fluid_type: str, substance: str, inputs: dict):
    result = satIceWatCalculation(fluid_type, inputs)
    return result

def handle_calculation_superheated134(fluid_type: str, substance: str, inputs: dict):
    result = sh_134a(fluid_type, inputs)
    return result

def handle_calculation_molGCP(fluid_type: str, substance: str):
    result = molGCPCalculation(substance)
    return result

def handle_calculation_specHeat300(fluid_type: str, substance: str):
    result = idealGas300KCalculation(substance)
    return result

def handle_calculation_specHeat(fluid_type: str, substance: str, inputs: dict):
    result = specHeatCalculation(substance, inputs)
    return result

def handle_calculation_idealGas(fluid_type: str, substance: str, inputs: dict):
    return IdealGasProperties(substance, inputs).calculate()

