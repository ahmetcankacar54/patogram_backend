from typing import List
from pydantic import BaseModel, Field, conint
from schemas.image import ImageBase


class FollowBase(BaseModel):
    user_id: int = Field(default=None)
    post_id: int = Field(default=None)
    follow_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True


class SetFollowBase(BaseModel):
    post_id: int = Field(default=None)
    follow_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True
