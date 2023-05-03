from typing import Optional
from pydantic import BaseModel, Field, StrictBool


class PollBase(BaseModel):
    id: int = Field(default=None)
    user_id: int = Field(default=None)
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
    isChosen: bool

    class Config:
        orm_mode = True


class GetPostResponseModel(BaseModel):
    isChosen: bool

    class Config:
        orm_mode = True
