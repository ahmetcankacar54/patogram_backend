from database.configuration import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Like(BaseModel):
    __tablename__ = "likes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    comment_id = Column(Integer, ForeignKey(
        "comments.id", ondelete="CASCADE"))
    like_owner = relationship("models.user.User")
    comment = relationship("models.comment.Comment")
