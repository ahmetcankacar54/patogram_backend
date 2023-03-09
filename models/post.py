from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from models import BaseModel
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(BaseModel):
    __tablename__ = "posts"

    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default= text('now()'),nullable= False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)

 
