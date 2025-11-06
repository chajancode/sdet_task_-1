from pydantic import BaseModel, Field


class GetAllParamsModel(BaseModel):
    title: str | None = Field(
        default=None
    )
    verified: bool | None = Field(
        default=None
    )
    page: int | None = Field(
        default=None,
        ge=1
    )
    per_page: int | None = Field(
        alias_priority="perPage",
        ge=1
    )
