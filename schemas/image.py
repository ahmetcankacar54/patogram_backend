from typing import List, Text
from pydantic import BaseModel, Field

class ImageBase(BaseModel):
    bs64Text: str = Field(List[Text])

class ConvertImage(ImageBase):
    pass

