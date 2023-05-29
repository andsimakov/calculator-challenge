from typing import Any

from constants import ResponseColor


def parse_data_to_rpn(data: dict[str, Any], precedence: dict[str, int]) -> list[Any]:
    operands = data["operands"]
    operators = data["operators"]
    rpn = []
    operator_stack = []

    for operand in operands:
        rpn.append(operand)

        if operators:
            operator = operators.pop(0)
            if operator not in precedence:
                raise ValueError(f"Unsupported operator: {operator}")

            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(operator, 0):
                rpn.append(operator_stack.pop())

            operator_stack.append(operator)

    rpn.extend(operator_stack[::-1])

    return rpn


def evaluate_color(number: float) -> [ResponseColor | None]:
    if number == int(number):
        return ResponseColor.GREEN if number % 2 == 0 else ResponseColor.RED
    else:
        return None
