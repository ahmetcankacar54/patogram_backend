from pydantic import Field, conint
from database.configuration import Base


class Like(Base):
    __tablename__ = "likes"
    user_id: int = Field(default=None)
    comment_id: int = Field(default=None)
    like_status: conint(le=1) = Field(default=None)
    isLike: bool = True

    class Config:
        orm_mode = True
