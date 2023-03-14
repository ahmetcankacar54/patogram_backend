from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from security import oauth2
import services
from schemas import CommentBase, CommentOut



router = APIRouter(
    prefix="/api/comment",
    tags=['Comment']
)

@router.get("/{post_id}", status_code=status.HTTP_201_CREATED, response_model= List[CommentOut])
async def get_comments(post_id:int, db: Session = Depends(get_db)):

    return await services.get_comments(db)
    

@router.post("/{post_id}", status_code=status.HTTP_201_CREATED, response_model=CommentOut)
async def create_comment(post_id: int, comment: CommentBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.create_comment(post_id, current_user.id, comment, db)

