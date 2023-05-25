from typing import List
from pydantic import BaseModel, Field


class PollBase(BaseModel):
    id: int = Field(default=None)
    post_id: int = Field(default=None)
    item: str = Field(default=None)
    isVote: bool = Field(default=False)

    class Config:
        orm_mode = True


class PollCreate(BaseModel):
    item: str = Field(default=None)

    class Config:
        orm_mode = True


class GetPollResultResponseModel(BaseModel):
    id: int = Field(default=None)
    item: str = Field(default=None)
    votes: int = Field(default=None)
    percentage: float = Field(default=None)

    class Config:
        orm_mode = True
