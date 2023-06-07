from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from models import BaseModel
from sqlalchemy.orm import relationship


class UserFollow(BaseModel):
    __tablename__ = "user_follows"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    follows_id = Column(Integer, nullable=False)
    isFollow = Column(Boolean, server_default="True", nullable=False)
    userId = relationship("models.user.User")
