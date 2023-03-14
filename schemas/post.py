from pydantic import BaseModel,Field
from datetime import datetime
from schemas.user import UserSchema

class PostBase(BaseModel):
    title: str = Field(default=None)
    content: str = Field(default=None)
    published: bool = True

class CreatePost(PostBase):
    pass

class PostOut(PostBase):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    #comment: int
    owner_id: int = Field(default=None)
    owner: UserSchema

    class Config:
        orm_mode = True
