from models import Comment
from models.like import Like
from schemas import CreateComment
from fastapi import Depends
from database.configuration import get_db
from sqlalchemy.orm import Session


async def get_comments(post_id: int, db: Session = Depends(get_db)):

    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    for comment in comments:
        likes = db.query(Like).filter(Like.comment_id == comment.id).count()
        comment.likes = likes

    return comments


async def create_comment(post_id: int, user_id: int, comment: CreateComment, db: Depends(get_db)):

    new_comment = Comment(**comment.dict())

    new_comment.owner_id = user_id
    new_comment.post_id = post_id

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment
