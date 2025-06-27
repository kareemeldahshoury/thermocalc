from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.calculationRequest import CalculationRequest
from backend.controller.calculationController import ( handle_calculation_satwater, handle_calculation_superHeatedWater, handle_calculation_idealAir, handle_calculation_N2, handle_calculation_O2,
handle_calculation_CO2, handle_calculation_CO, handle_calculation_H2)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Maybe switch back to port 5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/calculate/satwater")
def calculate_satwater(req: CalculationRequest):
    try:
        result = handle_calculation_satwater(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    

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
    
@app.post("/api/calculate/idealAir")
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


@app.post("/api/calculate/idealN2")
def calculate_idealN2(req: CalculationRequest):
    try:
        result = handle_calculation_N2(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/idealO2")
def calculate_idealO2(req: CalculationRequest):
    try:
        result = handle_calculation_O2(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/idealCO2")
def calculate_idealCO2(req: CalculationRequest):
    try:
        result = handle_calculation_CO2(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/idealCO")
def calculate_idealCO(req: CalculationRequest):
    try:
        result = handle_calculation_CO(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

@app.post("/api/calculate/idealH2")
def calculate_idealH2(req: CalculationRequest):
    try:
        result = handle_calculation_H2(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
