import enum

from api.calculation_strategies import AdditionStrategy, DivisionStrategy, MultiplicationStrategy, SubtractionStrategy


PROJECT_NAME = "Calculator Challenge"
PROJECT_VERSION = "1.0.0"
MATH_PRECEDENCE = {"*": 2, "/": 2, "+": 1, "-": 1}
MATH_OPERATORS = {
    "+": AdditionStrategy(),
    "-": SubtractionStrategy(),
    "*": MultiplicationStrategy(),
    "/": DivisionStrategy(),
}


class ResponseColor(enum.Enum):
    RED = "red"
    GREEN = "green"
