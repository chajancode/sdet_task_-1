from typing import List
from pydantic import BaseModel

from models.get_response_model import ResponseModel


class GetAllResponseModel(BaseModel):
    entity: List[ResponseModel]
