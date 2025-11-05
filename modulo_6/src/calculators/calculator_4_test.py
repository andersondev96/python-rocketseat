from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
  def __init__(self, body) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
  calculator_4 = Calculator4()

  response = calculator_4.calculate(mock_request)

  # Formato da resposta
  assert "data" in response
  assert "Calculator" in response["data"]
  assert "value" in response["data"]

  # assertividade da resposta
  assert response["data"]["Calculator"] == 4
  assert response["data"]["value"] == 3.0
  assert response["data"]["Success"] == True

def test_calculate_with_empty_list():
  mock_request = MockRequest({ "numbers": [] })
  calculator_4 = Calculator4()

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "body mal formatado!"

def test_calculate_with_non_list():
  mock_request = MockRequest({ "numbers": 123 })
  calculator_4 = Calculator4()

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "body mal formatado!"

def test_calculate_with_invalid_types():
  mock_request = MockRequest({ "numbers": [1, 2, "three", 4] })
  calculator_4 = Calculator4()

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "body mal formatado!"
