from typing import Optional

from fastapi import APIRouter, Header, HTTPException

from api.calculation_context import CalculationContext
from api.constants import MATH_OPERATORS, MATH_PRECEDENCE, PROJECT_NAME, PROJECT_VERSION
from api.schema import CalculationRequest
from api.utils import evaluate_color, parse_data_to_rpn


router = APIRouter()

calculation_context = CalculationContext(MATH_OPERATORS)


@router.get("/", summary="API Info", description="Get API Info")
async def root():
    return {"message": f"{PROJECT_NAME} v{PROJECT_VERSION}"}


@router.post(
    "/calculations", summary="Do calculations", description="Do calculations with given operands and operators"
)
async def calculate(request: CalculationRequest, pass_color: Optional[bool] = Header(False)):
    try:
        rpn = parse_data_to_rpn(dict(request), MATH_PRECEDENCE)
        result = calculation_context.calculate_rpn(rpn)

        response = {"result": result}
        response_color = evaluate_color(result)
        if pass_color and response_color:
            response["color"] = response_color.value

        return response
    except (ValueError, ZeroDivisionError) as e:
        raise HTTPException(status_code=400, detail=str(e))
