from pydantic import BaseModel,Field
from datetime import datetime

class PostBase(BaseModel):
    title: str = Field(default=None)
    content: str = Field(default=None)
    published: bool = True

class CreatePost(PostBase):
    pass

class PostOut(PostBase):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    owner_id: int = Field(default=None)

    class Config:
        orm_mode = True
