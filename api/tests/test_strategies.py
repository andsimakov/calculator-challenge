import pytest

from api.calculation_strategies import AdditionStrategy, DivisionStrategy, MultiplicationStrategy, SubtractionStrategy
from api.schema import CalculationRequest


class TestStrategies:
    @pytest.fixture
    def calculation_request(self):
        return CalculationRequest(operand1=2, operand2=3)

    def test_addition_strategy(self):
        strategy = AdditionStrategy()
        assert strategy.calculate(2, 3) == 5

    def test_subtraction_strategy(self):
        strategy = SubtractionStrategy()
        assert strategy.calculate(5, 3) == 2

    def test_multiplication_strategy(self):
        strategy = MultiplicationStrategy()
        assert strategy.calculate(2, 3) == 6

    def test_division_strategy(self):
        strategy = DivisionStrategy()
        assert strategy.calculate(6, 3) == 2
