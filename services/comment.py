from models import Comment
from schemas import CreateComment, CommentBase
from fastapi import  Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session

async def get_comments(db: Session = Depends(get_db)):
    comments = db.query(Comment).all()
    return comments

async def create_comment(post_id: int, user_id: int, comment: CreateComment, db: Depends(get_db)):    

    new_comment = Comment(**comment.dict())
    
    new_comment.owner_id = user_id
    new_comment.post_id = post_id

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment