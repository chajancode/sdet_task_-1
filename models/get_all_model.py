from typing import List
from pydantic import BaseModel

from models.response_model import ResponseModel


class GetAllModel(BaseModel):
    entity: List[ResponseModel]
