from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models import BaseModel


class Poll(BaseModel):
    __tablename__ = "polls"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    item = Column(String(length=180, collation="en_US.utf8",
                  convert_unicode=False, unicode_error=None), nullable=False)
    isChosen = Column(Boolean, server_default='False', nullable=False)
    poll_owner = relationship("models.user.User")
    post = relationship("models.post.Post")
