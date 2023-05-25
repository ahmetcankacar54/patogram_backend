from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.follow import SetFollowBase
from security import oauth2
import services

router = APIRouter(
    prefix="/api/follow",
    tags=['Follow']
)


@router.post("/set", status_code=status.HTTP_200_OK)
async def set_follow(follow: SetFollowBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.set_follow(follow, current_user.id, db)
