import pytest

from api.calculation_context import CalculationContext
from api.constants import MATH_OPERATORS


@pytest.mark.parametrize("rpn,expected", [([3.0, 4.0, "+"], 7.0), ([3, 4, "+", 2, 1, "/", "-", 5, 2, "*", "+"], 15.0)])
def test_calculation_context(rpn, expected):
    calculation_context = CalculationContext(MATH_OPERATORS)
    calculation_context.calculate_rpn(rpn)
