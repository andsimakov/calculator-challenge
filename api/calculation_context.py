from typing import Any

from api.calculation_strategies import CalculationStrategy


class CalculationContext:
    def __init__(self, strategies: dict[str, CalculationStrategy]) -> None:
        self.strategies = strategies

    def calculate_rpn(self, expression: list[Any]) -> float:
        stack = []

        for token in expression:
            if not isinstance(token, str):
                stack.append(float(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token in self.strategies:
                    strategy = self.strategies[token]
                    result = strategy.calculate(operand1, operand2)
                    stack.append(result)
                else:
                    raise ValueError(f"Unsupported operator: {token}")

        return stack[0]
