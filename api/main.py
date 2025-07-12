from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.calculationRequest import CalculationRequest
from backend.controller.calculationController import ( handle_calculation_superHeatedWater, handle_calculation_idealAir,
handle_calculation_superheated134, handle_calculation_molGCP, handle_calculation_specHeat300, handle_calculation_specHeat, handle_calculation_idealGas, handle_calculation_saturatedFluid,
handle_unit_conversion)
from pydantic import BaseModel
from typing import Union
from backend.models.unitConversionModel import UnitConversionRequest


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Maybe switch back to port 5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/calculate/superHeatedWater")
def calculate_superHeatedWater(req: CalculationRequest):
    try:
        result = handle_calculation_superHeatedWater(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/airData")
def calculate_idealAir(req: CalculationRequest):
    try:
        result = handle_calculation_idealAir(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

    
@app.post("/api/calculate/superheatedR134")
def calculate_sh134a(req: CalculationRequest):
    try:
        result = handle_calculation_superheated134(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    

@app.post("/api/calculate/molGCP")
def calculate_molGCP(req: CalculationRequest):
    try:
        result = handle_calculation_molGCP(
            fluid_type=req.fluidType,
            substance=req.substance
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/specHeat300")
def calculate_specHeat300(req: CalculationRequest):
    try:
        result = handle_calculation_specHeat300(
            fluid_type=req.fluidType,
            substance=req.substance
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

@app.post("/api/calculate/specHeat")
def calculate_specHeat(req: CalculationRequest):
    try:
        # Optionally validate temperature exists
        if "temperature" not in req.inputs:
            raise ValueError("Temperature is required for specHeat calculation.")
        
        result = handle_calculation_specHeat(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

@app.post("/api/calculate/idealGas")
def calculate_idealGas(req: CalculationRequest):
    try:
        if "temperature" not in req.inputs:
            raise ValueError("Temperature is required.")

        result = handle_calculation_idealGas(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/satFluid")
def calculate_saturatedFluid(req: CalculationRequest):
    try:
        result = handle_calculation_saturatedFluid(
            fluid_type=req.fluidType,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/unitConversion")
def calculate_unit_conversion(req: UnitConversionRequest):
    try:
        result = handle_unit_conversion(
            from_unit=req.from_unit,
            to_unit=req.to_unit,
            value=req.input_value
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}