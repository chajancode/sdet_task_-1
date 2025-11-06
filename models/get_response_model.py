from typing import List

from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int
    id: int


class GetResponseModel(BaseModel):
    addition: Addition
    id: int
    important_numbers: List[int]
    title: str
    verified: bool

