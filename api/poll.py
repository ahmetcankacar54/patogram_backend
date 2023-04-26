from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from models.poll import Poll
from schemas.poll import PollBase
from security import oauth2
import services


router = APIRouter(
    prefix="/api/poll",
    tags=['Poll']
)


@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def create_poll(id: int, db: Session = Depends(get_db)):
    poll = db.query(Poll).filter(Poll.id == id).first()
    return poll
