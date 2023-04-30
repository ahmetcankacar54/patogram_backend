from typing import List
from pydantic import BaseModel, Field, conint
from schemas.image import ImageBase


class FavoriteBase(BaseModel):
    user_id: int = Field(default=None)
    post_id: int = Field(default=None)
    fav_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True


class PostFavorite(BaseModel):
    id: int = Field(default=None)
    images: List[ImageBase]

    class Config:
        orm_mode = True


class SetFavoriteBase(BaseModel):
    post_id: int = Field(default=None)
    fav_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True


class FavoriteOut(BaseModel):
    post: List[PostFavorite]

    class Config:
        orm_mode = True
