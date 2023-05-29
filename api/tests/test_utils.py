import pytest

from api.constants import MATH_PRECEDENCE, ResponseColor
from api.utils import evaluate_color, parse_data_to_rpn


class TestUtils:
    def test_evaluate_color_with_positive_even_int_should_return_color(self):
        result = evaluate_color(4)
        assert result.value == ResponseColor.GREEN.value

    def test_evaluate_color_with_positive_odd_int_should_return_color(self):
        result = evaluate_color(7)
        assert result.value == ResponseColor.RED.value

    def test_evaluate_color_with_positive_float_should_return_none(self):
        result = evaluate_color(3.5)
        assert result is None

    def test_evaluate_color_with_negative_even_int_should_return_color(self):
        result = evaluate_color(-6)
        assert result.value == ResponseColor.GREEN.value

    def test_evaluate_color_with_negative_odd_int_should_return_color(self):
        result = evaluate_color(-9)
        assert result.value == ResponseColor.RED.value

    def test_evaluate_color_with_zero_should_return_color(self):
        result = evaluate_color(0)
        assert result.value == ResponseColor.GREEN.value

    @pytest.mark.parametrize(
        "data,expected",
        [
            ({"operands": [3.0, 4.0], "operators": ["+"]}, [3.0, 4.0, "+"]),
            (
                {"operands": [3, 4, 2, 1, 5, 2], "operators": ["+", "-", "/", "+", "*"]},
                [3, 4, "+", 2, 1, "/", "-", 5, 2, "*", "+"],
            ),
        ],
    )
    def test_parse_data_to_rpn(self, data, expected):
        assert parse_data_to_rpn(data, MATH_PRECEDENCE) == expected
