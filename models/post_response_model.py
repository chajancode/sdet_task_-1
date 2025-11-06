from pydantic import BaseModel


class PostResponseModel(BaseModel):
    value: str
