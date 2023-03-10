from database.configuration import Base
from sqlalchemy import TIMESTAMP, Column, Integer, text


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default= text('now()'),nullable= False)
