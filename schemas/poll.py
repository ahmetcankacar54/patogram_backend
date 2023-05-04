from typing import List
from pydantic import BaseModel, Field

from schemas.vote import PollResponseModel


class PollBase(BaseModel):
    id: int = Field(default=None)
    post_id: int = Field(default=None)
    item: str = Field(default=None)

    class Config:
        orm_mode = True


class PollCreate(BaseModel):
    item: str = Field(default=None)

    class Config:
        orm_mode = True


class GetPollResponseModel(BaseModel):
    id: int = Field(default=None)
    item: str = Field(default=None)
    votes: int = Field(default=None)
    percentage: float = Field(default=None)

    class Config:
        orm_mode = True


class GetPostResponseModel(PollBase):
    isChosen: List[PollResponseModel]

    class Config:
        orm_mode = True
