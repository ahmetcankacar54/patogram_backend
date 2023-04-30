from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    image: str = Field(default=None)
    thumbnail: str = Field(default=None)
    zoom_amount: str = Field(default=None)

    class Config:
        orm_mode = True


class CreatePostImageModel(BaseModel):
    image: str = Field(default=None)
    zoom_amount: str = Field(default=None)

    class Config:
        orm_mode = True
