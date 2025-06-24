from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import CalculationRequest
from backend.controller import handle_calculation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/calculate")
def calculate(req: CalculationRequest):
    try:
        result = handle_calculation(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

