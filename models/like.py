from pydantic import validator
from database.configuration import Base
from sqlalchemy import Boolean, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Like(BaseModel):
    __tablename__ = "likes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    comment_id = Column(Integer, ForeignKey(
        "comments.id", ondelete="CASCADE"))
    isLike = Column(Boolean, server_default='False', nullable=False)
    like_owner = relationship("models.user.User")
    comment = relationship("models.comment.Comment", overlaps="liked")
    like = relationship("models.comment.Comment", overlaps="like, comment")
