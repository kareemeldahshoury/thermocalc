from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.calculationRequest import CalculationRequest
from backend.controller.calculationController import ( handle_calculation_satwater, handle_calculation_superHeatedWater, handle_calculation_idealAir, handle_calculation_N2, handle_calculation_O2,
handle_calculation_CO2, handle_calculation_CO, handle_calculation_H2, handle_calculation_H2O, handle_calculation_O, handle_calculation_OH, handle_calculation_satR134, handle_calculation_satIceWat,
handle_calculation_superheated134, handle_calculation_molGCP, handle_calculation_specHeat300)

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

@app.post("/api/calculate/idealH2O")
def calculate_idealH2O(req: CalculationRequest):
    try:
        result = handle_calculation_H2O(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/idealO")
def calculate_idealO(req: CalculationRequest):
    try:
        result = handle_calculation_O(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}

@app.post("/api/calculate/idealOH")
def calculate_idealOH(req: CalculationRequest):
    try:
        result = handle_calculation_OH(
            fluid_type=req.fluidType,
            substance=req.substance,
            inputs=req.inputs
        )
        return {"result": result}
    except ValueError as e:
        return {"result": f"Error: {str(e)}"}
    except Exception as e:
        return {"result": f"Unexpected error: {str(e)}"}
    
@app.post("/api/calculate/satIceWat")
def calculate_satIceWat(req: CalculationRequest):
    try:
        result = handle_calculation_satIceWat(
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
    

@app.post("/api/calculate/satR134")
def calculate_sat134(req: CalculationRequest):
    try:
        result = handle_calculation_satR134(
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
def calculate_specHEat300(req: CalculationRequest):
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
