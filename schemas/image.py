from typing import List, Text
from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    image: str = Field(default=None)
    zoom_amount: str = Field(default=None)

    class Config:
        orm_mode = True


class Images(BaseModel):
    image: str = Field(default=None)
    thumbnail: str = Field(default=None)
    zoom_amount: str = Field(default=None)
    class Config:
        orm_mode = True
