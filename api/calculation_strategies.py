from abc import ABC, abstractmethod


class CalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, operand1: float, operand2: float) -> float:
        pass


class AdditionStrategy(CalculationStrategy):
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 + operand2


class SubtractionStrategy(CalculationStrategy):
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 - operand2


class MultiplicationStrategy(CalculationStrategy):
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 * operand2


class DivisionStrategy(CalculationStrategy):
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 / operand2
