from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Image(BaseModel):
    __tablename__ = "images"

    imageUrl = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    post = relationship("Post")
    post_1 = relationship("Post")
