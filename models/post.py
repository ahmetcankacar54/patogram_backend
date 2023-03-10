from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from models import BaseModel

class Post(BaseModel):
    __tablename__ = "posts"

    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)

 
