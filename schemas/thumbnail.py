from typing import List, Text
from pydantic import BaseModel, Field


class Thumbnail(BaseModel):
    thumbnail: str = Field(default=None)

    class Config:
        orm_mode = True
