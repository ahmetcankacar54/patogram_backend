from fastapi import Depends
from requests import Session
from database.configuration import get_db
from models import Vote, Poll
from schemas.poll import PollCreate


async def get_poll(post_id: int, db: Session = Depends(get_db)):
    polls = db.query(Poll).filter(Poll.post_id == post_id).all()
    poll_list = []
    total_votes = 0
    n = -1

    for poll in polls:
        votes = db.query(Vote).filter(Vote.poll_id == poll.id).count()
        print(type(poll.isChosen))
        poll.votes = votes
        poll_list.append(poll)
        total_votes += votes
        n = n+1

    while n > -1:
        vote = poll_list[n]
        if vote.votes > 0:
            percent = (vote.votes/total_votes)*100
            percent = round(percent, 2)
            vote.percentage = percent
        elif vote.votes == 0:
            vote.percentage = 0
        n -= 1

    return poll_list


async def add_poll(polls: PollCreate, user_id: int, post_id: int, db: Depends(get_db)):
    poll = Poll(**polls.dict())
    poll.user_id = user_id
    poll.post_id = post_id
    poll.item = polls.item
    db.add(poll)
    db.commit()
    db.refresh(poll)

    return {"message": "Successfull"}
