from pydantic import BaseModel, Field

class UnitConversionRequest(BaseModel):
    input_value: float = Field(..., alias="inputValue")
    from_unit: str = Field(..., alias="fromUnit")
    to_unit: str = Field(..., alias="toUnit")

    class Config:
        allow_population_by_field_name = True  # ✅ REQUIRED for FastAPI to use aliases
        extra = "forbid"  # Optional: reject unknown fields
