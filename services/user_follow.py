from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from models.favorite import Favorite
from models.post import Post
from models.user_follow import UserFollow
from models.case_follow import Follow
from models.user import User
from schemas.user_follow import SetFollowsBase


async def get_follows_cases(current_user: int, db: Session = Depends(get_db)):
    user_query = db.query(UserFollow).filter(UserFollow.user_id == current_user).all()
    postList = []
    for i in user_query:
        post_query = db.query(Post).filter(Post.owner_id == i.follows_id).all()
        for p in post_query:
            favorite_querry = (
                db.query(Favorite)
                .filter(
                    Favorite.post_id == p.id,
                    Favorite.user_id == current_user,
                    Favorite.isFavorite == True,
                )
                .first()
            )
            if favorite_querry:
                p.isFavorite = True
            else:
                p.isFavorite = False

            follow_querry = (
                db.query(Follow)
                .filter(
                    Follow.post_id == p.id,
                    Follow.user_id == current_user,
                    Follow.isFollow == True,
                )
                .first()
            )
            if follow_querry:
                p.isFollow = True
                postList.append(p)
            else:
                p.isFollow = False
                postList.append(p)

    return postList


async def set_follow(
    follow: SetFollowsBase, current_user: int, db: Session = Depends(get_db)
):
    follow_request = SetFollowsBase(**follow.dict())
    followersNumber: int

    follows = db.query(User).filter(User.id == follow_request.follows_id).first()
    if not follows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!"
        )

    if follow_request.follow_status == 1:
        new_follow = UserFollow(
            user_id=current_user,
            follows_id=follow_request.follows_id,
            isFollow=follow_request.follow_status,
        )
        db.add(new_follow)
        db.commit()
        db.refresh(new_follow)
    else:
        follow_querry = db.query(UserFollow).filter(
            UserFollow.user_id == current_user,
            UserFollow.follows_id == follow_request.follows_id,
        )

        follow_querry.delete(synchronize_session=False)
        db.commit()
    followersNumber = (
        db.query(UserFollow)
        .filter(UserFollow.follows_id == follow_request.follows_id)
        .count()
    )
    return followersNumber
