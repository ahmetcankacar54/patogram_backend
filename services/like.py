from fastapi import Depends, HTTPException, status
from requests import Session
from database.configuration import get_db
from models import Like, Comment


"""async def count_likes(db: Session = Depends(get_db)):
    
    return await services.count_likes(db)"""


async def like(comment_id: int, like_status: int, user_id: int, db: Session = Depends(get_db)):

    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment not found!")

    like_query = db.query(Like).filter(
        Like.comment_id == comment_id, Like.user_id == user_id)

    found_like = like_query.first()
    if (like_status == 1):
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,

                                detail=f"Alredy liked the comment!")
        new_like = Like(comment_id=comment_id, user_id=user_id)
        db.add(new_like)
        db.commit()
        return {"message": "successfully added like"}
    else:
        like_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted like"}
