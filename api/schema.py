from pydantic import BaseModel


class CalculationRequest(BaseModel):
    operands: list[float]
    operators: list[str]
