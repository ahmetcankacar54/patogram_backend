from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Image(BaseModel):
    __tablename__ = "images"

    image = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    post_id = Column(
        Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
    zoom_amount = Column(String, nullable=False)
    paint_type = Column(String, nullable=False)
    post = relationship("models.post.Post", overlaps="thumbnail")
    post_1 = relationship("models.post.Post", overlaps="images,post")
