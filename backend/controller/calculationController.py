from backend.service.satWaterService import sat_water
from backend.service.superHeatedWaterService import sh_water
from backend.service.idealAirService import idealAirCalculation
from backend.service.idealN2Service import idealN2Calculation
from backend.service.idealO2Service import idealO2Calculation
from backend.service.idealCO2Service import idealCO2Calculation
from backend.service.idealCOService import idealCOCalculation
from backend.service.idealH2Service import idealH2Calculation
from backend.service.idealH2OService import idealH2OCalculation
from backend.service.idealOService import idealOCalculation
from backend.service.idealOHService import idealOHCalculation
from backend.service.satR134Service import sat_r134
from backend.service.satIceWatService import satIceWatCalculation


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

def handle_calculation_O2(fluid_type: str, substance: str, inputs: dict):
    result = idealO2Calculation(fluid_type, inputs)
    return result

def handle_calculation_CO2(fluid_type: str, substance: str, inputs: dict):
    result = idealCO2Calculation(fluid_type, inputs)
    return result

def handle_calculation_CO(fluid_type: str, substance: str, inputs: dict):
    result = idealCOCalculation(fluid_type, inputs)
    return result

def handle_calculation_H2(fluid_type: str, substance: str, inputs: dict):
    result = idealH2Calculation(fluid_type, inputs)
    return result

def handle_calculation_H2O(fluid_type: str, substance: str, inputs: dict):
    result = idealH2OCalculation(fluid_type, inputs)
    return result

def handle_calculation_O(fluid_type: str, substance: str, inputs: dict):
    result = idealOCalculation(fluid_type, inputs)
    return result

def handle_calculation_OH(fluid_type: str, substance: str, inputs: dict):
    result = idealOHCalculation(fluid_type, inputs)
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
