from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    profile_image = Column(String, nullable=True)
    user_bio = Column(String, nullable=True)
    posts = relationship("models.post.Post", back_populates="post_owner")
    userComment = relationship(
        "models.comment.Comment", back_populates="comment_owner")
    likes = relationship("models.like.Like", back_populates="like_owner")
    favorites = relationship(
        "models.favorite.Favorite", back_populates="userId")
    polls = relationship("models.poll.Poll", back_populates="poll_owner")
