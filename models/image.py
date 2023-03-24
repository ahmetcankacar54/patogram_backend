from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel

class Image(BaseModel):
    __tablename__ = "images"

    imageUrl = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable= False)
    post = relationship("Post")
