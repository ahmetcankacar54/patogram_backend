from fastapi import Depends, HTTPException, status
from requests import Session
from database.configuration import get_db
from models import Vote, Poll
from schemas.vote import AddVote


async def vote(votes: AddVote, user_id: int, db: Session = Depends(get_db)):
    vote = AddVote(**votes.dict())
    poll_id = vote.poll_id
    vote_status = vote.vote_status
    post_id = vote.post_id

    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Poll not found!")

    vote_query = db.query(Vote).filter(
        Vote.poll_id == poll_id, Vote.user_id == user_id)
    is_vote_querry = db.query(Vote).filter(
        Vote.post_id == post_id, Vote.user_id == user_id)

    is_vote = is_vote_querry.first()

    found_vote = vote_query.first()
    if (vote_status == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,

                                detail=f"Alredy voted!")
        elif is_vote:
            is_vote_querry.delete(synchronize_session=False)
            db.commit()

        new_vote = Vote(poll_id=poll_id, user_id=user_id,
                        post_id=post_id, isVote=True)
        db.add(new_vote)
        db.commit()
    else:
        vote_query.delete(synchronize_session=False)
        db.commit()

    return {}
