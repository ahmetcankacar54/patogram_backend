from sqlalchemy import Column,Integer,String
from db.base_class import Base

class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)