from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from models.case_follow import Follow
from models.post import Post
from schemas.case_follow import FollowBase, SetFollowBase


async def set_follow(
    follow: SetFollowBase, current_user: int, db: Session = Depends(get_db)
):
    follow_request = FollowBase(**follow.dict())

    post = db.query(Post).filter(Post.id == follow_request.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!"
        )

    if follow_request.follow_status == 1:
        new_follow = Follow(
            user_id=current_user,
            post_id=follow_request.post_id,
            isFollow=follow_request.follow_status,
        )
        db.add(new_follow)
        db.commit()
        db.refresh(new_follow)
    else:
        follow_querry = db.query(Follow).filter(
            Follow.user_id == current_user, Follow.post_id == follow_request.post_id
        )

        follow_querry.delete(synchronize_session=False)
        db.commit()
    return {"message": "successfull"}
