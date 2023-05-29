import pytest

from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


class TestE2ECalculations:
    def test_calculate_endpoint_with_correct_input_should_return_float(self, client):
        request_data = {"operands": [3, 4, 2, 1, 5, 2], "operators": ["+", "-", "/", "+", "*"]}
        response = client.post("api/v1/calculations/", json=request_data)

        assert response.status_code == 200
        assert response.json() == {"result": 15.0}

    def test_calculate_endpoint_with_incorrect_operator_should_return_error(self, client):
        operator = "^"
        request_data = {"operands": [3, 4], "operators": [operator]}
        response = client.post("api/v1/calculations/", json=request_data)

        assert response.status_code == 400
        assert response.json() == {"detail": f"Unsupported operator: {operator}"}

    def test_calculate_endpoint_with_zero_division_should_return_error(self, client):
        request_data = {"operands": [2, 0], "operators": ["/"]}
        response = client.post("api/v1/calculations/", json=request_data)

        assert response.status_code == 400
        assert response.json() == {"detail": "float division by zero"}
