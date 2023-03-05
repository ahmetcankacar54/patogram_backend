import datetime
from database.configuration import Base
from sqlalchemy import Column, Integer, DateTime


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
