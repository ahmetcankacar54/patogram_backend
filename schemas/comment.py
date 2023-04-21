from pydantic import BaseModel, Field
from datetime import datetime
from schemas.user import UserSchema


class CommentBase(BaseModel):
    content: str = Field(default=None)
    published: bool = True


class CreateComment(CommentBase):
    pass


class CommentOut(CommentBase):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    likes: int = Field(default=None)
    liked: bool = Field(default=None)
    comment_owner: UserSchema

    class Config:
        orm_mode = True
