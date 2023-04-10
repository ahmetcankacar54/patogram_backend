from typing import List, Text
from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    imageUrl: str = Field(default=None)

    class Config:
        orm_mode = True


class ThumbNail(BaseModel):
    thumbnail: str = Field(default=None)

    class Config:
        orm_mode = True
