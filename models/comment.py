from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from models import BaseModel
from sqlalchemy.orm import relationship


class Comment(BaseModel):
    __tablename__ = "comments"

    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable= False)
    owner = relationship("User")
    post = relationship("Post")

