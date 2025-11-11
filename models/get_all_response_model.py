from typing import List
from pydantic import BaseModel

from models.get_response_model import GetResponseModel


class GetAllResponseModel(BaseModel):
    entity: List[GetResponseModel]
