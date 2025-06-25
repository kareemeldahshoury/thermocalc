from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.calculationRequest import CalculationRequest
from backend.controller.calculationController import handle_calculation_satwater, handle_calculation_superHeatedWater

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Maybe switch back to port 5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/calculate/satwater")
def calculate(req: CalculationRequest):
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
def calculate(req: CalculationRequest):
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

