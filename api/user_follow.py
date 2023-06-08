from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.post import PostOut
from schemas.user_follow import SetFollowsBase
from security import oauth2
import services

router = APIRouter(prefix="/api/follows", tags=["User Follow"])


@router.get("/get", status_code=status.HTTP_200_OK, response_model=List[PostOut])
async def get_follow_cases(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    return await services.GetFollowsCases(current_user.id, db)


@router.post("/set", status_code=status.HTTP_200_OK)
async def set_user_follow(
    follow: SetFollowsBase,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.SetUserFollow(follow, current_user.id, db)
