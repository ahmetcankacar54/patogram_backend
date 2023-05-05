from sqlalchemy import Boolean, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Vote(BaseModel):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"))
    poll_id = Column(Integer, ForeignKey(
        "polls.id", ondelete="CASCADE"))
    isVote = Column(Boolean, server_default='False', nullable=False)
    vote_owner = relationship("models.user.User")
    post = relationship("models.post.Post")
    poll = relationship("models.poll.Poll", overlaps="isChosen")
    is_vote = relationship("models.poll.Poll", overlaps="votess, poll")
