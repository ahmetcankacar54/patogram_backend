from typing import List, Text
from pydantic import BaseModel, Field

class ImageBase(BaseModel):
    bs64Text: str = Field(default=None)

class ImageList(BaseModel):
    images: List[ImageBase]

