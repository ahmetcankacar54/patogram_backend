from sqlalchemy import Column, String, Integer
from database.configuration import Base
from sqlalchemy.orm import relationship


class Disease(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    disease_en = Column(String, nullable=False)
    disease_tr = Column(String, nullable=False)
