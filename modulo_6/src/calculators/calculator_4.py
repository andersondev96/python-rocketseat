from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def calculate(self, request: FlaskRequest): # pyright: ignore[reportInvalidTypeForm]
    body = request.json
    input_data = self.__validate_body(body)
    media = self.calculate_media(input_data)

    formated_response = self.__format_response(media)
    return formated_response

  def __validate_body(self, body: Dict) -> List[float]:  
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("body mal formatado!")
  
    input_data = body["numbers"]

    # Verifica se é uma lista
    if not isinstance(input_data, list):
      raise HttpUnprocessableEntityError("body mal formatado!")
    
    # Verifica se a lista está vazia
    if len(input_data) == 0:
      raise HttpUnprocessableEntityError("body mal formatado!")
    
    # Verifica se todos os elementos são números
    for num in input_data:
      if not isinstance(num, (int, float)):
        raise HttpUnprocessableEntityError("body mal formatado!")

    return input_data
  
  def calculate_media(self, numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)
  
  def __format_response(self, media: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "value": media,
        "Success": True
      }
    }