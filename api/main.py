from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.calculationRequest import CalculationRequest
from backend.controller.calculationController import ( handle_calculation_superHeatedWater, handle_calculation_idealAir,
handle_calculation_superheated134, handle_calculation_molGCP, handle_calculation_specHeat300, handle_calculation_specHeat, handle_calculation_idealGas, handle_calculation_saturatedFluid,
handle_unit_conversion)
from pydantic import BaseModel
from typing import Union
from backend.models.unitConversionModel import UnitConversionRequest
from fastapi.staticfiles import StaticFiles
import os
from backend.core.calculations.questions import questions_by_unit
import random
from fastapi import Body
from fastapi import APIRouter, Query
from backend.core.calculations.questions import (questions_firstLaw, questions_unitConversion)

app = FastAPI()

static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'static'))
app.mount("/static", StaticFiles(directory=static_dir), name="static")

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
    


@app.get("/api/practice/random")
def get_random_question(unit: str = Query(...)):
    if unit not in questions_by_unit:
        return {"error": f"Invalid unit category: {unit}"}

    questions = questions_by_unit[unit]
    q_id = random.choice(list(questions.keys()))
    q = questions[q_id]

    return {
        "id": q_id,
        "image": q["image"],
        "num_answers": len(q["answers"])
    }



@app.post("/api/practice/validate")
def validate_practice_answers(data: dict = Body(...)):
    unit = data.get("unit")
    q_id = data.get("id")
    user_answers = data.get("answers", [])

    if unit not in questions_by_unit:
        return {"error": "Invalid unit category"}

    unit_questions = questions_by_unit[unit]

    if q_id not in unit_questions:
        return {"error": "Invalid question ID for this unit"}

    correct_answers = unit_questions[q_id]["answers"]
    result = []

    for user, correct in zip(user_answers, correct_answers):
        try:
            result.append(abs(user - correct) / abs(correct) <= 0.05)
        except ZeroDivisionError:
            result.append(user == correct)

    return {
        "correct": result,
        "all_correct": all(result)
    }


@app.get("/api/practice/list_ids")
def list_question_ids(unit: str):
    # Assuming you store questions like questions_unitConversion, etc.
    unit_map = {
        "unitConversion": questions_unitConversion,
        "firstLaw": questions_firstLaw,
        # Add others
    }
    if unit not in unit_map:
        return {"error": "Invalid unit"}
    
    question_ids = list(unit_map[unit].keys())
    return {"ids": question_ids}


@app.get("/api/practice/get_by_id")
def get_question_by_id(id: str = Query(...), unit: str = Query(...)):
    if unit not in questions_by_unit:
        return {"error": f"Invalid unit category: {unit}"}

    questions = questions_by_unit[unit]

    if id not in questions:
        return {"error": f"Invalid question ID: {id}"}

    q = questions[id]
    return {
        "id": id,
        "image": q["image"],
        "num_answers": len(q["answers"])
    }
