from pydantic import BaseModel


class GetAndDeleteModel(BaseModel):
    id: int
