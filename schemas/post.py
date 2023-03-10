from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True
