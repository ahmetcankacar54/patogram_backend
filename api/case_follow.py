from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.case_follow import SetFollowBase
from security import oauth2
import services

router = APIRouter(prefix="/api/follow", tags=["Case Follow"])


@router.post("/set", status_code=status.HTTP_200_OK)
async def set_case_follow(
    follow: SetFollowBase,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.SetCaseFollow(follow, current_user.id, db)
