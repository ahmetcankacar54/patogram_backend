from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from security import oauth2
import services
from schemas import CommentOut


router = APIRouter(
    prefix="/api/like",
    tags=['Like']
)


@router.post("/{comment_id}/{like_status}", status_code=status.HTTP_200_OK)
async def like(comment_id: int, like_status: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.like(comment_id, like_status, current_user.id, db)
