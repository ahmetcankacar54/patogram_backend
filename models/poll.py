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
    votes = Column(Integer, nullable=True)
    poll_owner = relationship("models.user.User")
    post = relationship("models.post.Post")
    vote = relationship("models.vote.Vote", overlaps="vote",
                        back_populates="poll")
    isChosen = relationship(
        "models.vote.Vote", overlaps="vote", back_populates="is_vote")
