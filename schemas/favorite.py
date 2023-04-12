from typing import List
from pydantic import BaseModel, Field, conint
from database.configuration import Base
from schemas.post import PostOut


class FavoriteBase(BaseModel):
    user_id: int = Field(default=None)
    post_id: int = Field(default=None)
    fav_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True


class FavoriteOut(BaseModel):
    posts: List[PostOut]

    class Config:
        orm_mode = True
