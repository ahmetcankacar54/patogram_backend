from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from schemas.poll import GetPollResultResponseModel, PollBase, PollCreate
from security import oauth2
import services


router = APIRouter(prefix="/api/poll", tags=["Poll"])


@router.get(
    "/get/{post_id}", response_model=List[PollBase], status_code=status.HTTP_200_OK
)
async def get_polls(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.get_polls(post_id, current_user.id, db)


@router.get(
    "/get/result/{post_id}",
    response_model=List[GetPollResultResponseModel],
    status_code=status.HTTP_200_OK,
)
async def get_poll_result(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.get_poll_result(post_id, current_user.id, db)


@router.post("/add/{post_id}", status_code=status.HTTP_200_OK)
async def add_poll(
    polls: PollCreate,
    post_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.add_poll(polls, current_user.id, post_id, db)
