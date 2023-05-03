from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from schemas.poll import GetPollResponseModel, PollCreate
from security import oauth2
import services


router = APIRouter(
    prefix="/api/poll",
    tags=['Poll']
)


@router.get("/get/{post_id}", response_model=List[GetPollResponseModel], status_code=status.HTTP_200_OK)
async def get_poll(post_id: int, db: Session = Depends(get_db)):

    return await services.get_poll(post_id, db)


@router.post("/add/{post_id}", status_code=status.HTTP_200_OK)
async def add_poll(polls: PollCreate, post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.add_poll(polls, current_user.id, post_id, db)
