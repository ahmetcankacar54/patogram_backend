from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from schemas.vote import AddVote
from security import oauth2
import services


router = APIRouter(
    prefix="/api/vote",
    tags=['Vote']
)


@router.post("", status_code=status.HTTP_200_OK)
async def vote(vote: AddVote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.vote(vote, current_user.id, db)
