from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from models.post import Post
from models.user_follow import Follow
from models.user import User
from schemas.user_follow import FollowsBase, SetFollowsBase


async def get_follow_cases(current_user: int, db: Session = Depends(get_db)):
    user_query = db.query(Follow).filter(Follow.user_id == current_user).all()
    postList = []
    for i in user_query:
        post_query = db.query(Post).filter(Post.owner_id == i.follows_id).all()
        for i in post_query:
            postList.append(i)

    return postList


async def set_follow(
    follow: SetFollowsBase, current_user: int, db: Session = Depends(get_db)
):
    follow_request = FollowsBase(**follow.dict())

    follows = db.query(User).filter(User.id == follow_request.follows_id).first()
    if not follows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!"
        )

    if follow_request.follow_status == 1:
        new_follow = Follow(
            user_id=current_user,
            follows_id=follow_request.follows_id,
            isFollow=follow_request.follow_status,
        )
        db.add(new_follow)
        db.commit()
        db.refresh(new_follow)
    else:
        follow_querry = db.query(Follow).filter(
            Follow.user_id == current_user,
            Follow.follows_id == follow_request.follows_id,
        )

        follow_querry.delete(synchronize_session=False)
        db.commit()
    return {"message": "successfull"}
