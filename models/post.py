from sqlalchemy import Column, String, Boolean
from base import BaseModel

class Post(BaseModel):
    __tablename__ = "posts"

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)


