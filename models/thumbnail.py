from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Thumbnail(BaseModel):
    __tablename__ = "thumbnails"

    thumbnail = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    post = relationship("Post")
