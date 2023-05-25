from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from models import BaseModel
from sqlalchemy.orm import relationship


class Follow(BaseModel):
    __tablename__ = "follows"

    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    isFollow = Column(Boolean, server_default='True', nullable=False)
    user = relationship("models.user.User")
    post = relationship("models.post.Post")
