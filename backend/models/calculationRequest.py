from pydantic import BaseModel
from typing import Optional, Dict

class CalculationRequest(BaseModel):
    fluidType: str
    substance: Optional[str] = None
    inputs: Optional[Dict[str, float]] = None
