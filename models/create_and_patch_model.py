from typing import List
from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int


class MainModel(BaseModel):
    addition: Addition
    important_numbers: List[int]
    title: str
    verified: bool
