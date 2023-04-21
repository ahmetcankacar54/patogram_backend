from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from models import BaseModel
from sqlalchemy.orm import relationship


class Favorite(BaseModel):
    __tablename__ = "favorites"

    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    isFavorite = Column(Boolean, server_default='True', nullable=False)
    userId = relationship("models.user.User")
    post = relationship("models.post.Post", overlaps="isFavorite")
    Favorite = relationship("models.post.Post", overlaps="favorite, post")
