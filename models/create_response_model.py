from pydantic import BaseModel, StrictStr


class CreateResponseModel(BaseModel):
    value: StrictStr
