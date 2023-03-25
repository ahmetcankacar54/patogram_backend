from typing import List, Text
from pydantic import BaseModel, Field

class ImageBase(BaseModel):
    imageUrl: str = Field(default=None)

