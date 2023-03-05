from sqlalchemy import Column, String
from models import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    full_name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True )
    password = Column(String, nullable = False)

