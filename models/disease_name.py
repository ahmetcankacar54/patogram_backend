from sqlalchemy import Column, String, Integer
from database.configuration import Base


class DiseaseName(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    disease_en = Column(String, nullable=False)
    disease_tr = Column(String, nullable=False)
