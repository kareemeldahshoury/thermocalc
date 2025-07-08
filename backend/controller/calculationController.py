
from backend.service.superHeatedWaterService import sh_water
from backend.service.idealAirService import idealAirCalculation
from backend.service.superheatedR134Service import sh_134a
from backend.core.calculations.molGCP import molGCPCalculation
from backend.core.calculations.specHeat300 import idealGas300KCalculation
from backend.core.calculations.specHeat import specHeatCalculation
from backend.core.calculations.idealGasCalculation import IdealGasProperties
from backend.core.calculations.saturatedFluidsCalc import SaturatedFluidCalculation

    
def handle_calculation_superHeatedWater(fluid_type: str, substance: str, inputs: dict):
    result = sh_water(fluid_type, inputs)
    return result
    
def handle_calculation_idealAir(fluid_type: str, substance: str, inputs: dict):
    result = idealAirCalculation(fluid_type, inputs)
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

def handle_calculation_saturatedFluid(fluid_type: str, inputs: dict):
    return SaturatedFluidCalculation(fluid_type, inputs).calculate()
