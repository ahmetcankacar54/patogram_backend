from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from models.favorite import Favorite
from models.post import Post
from schemas.favorite import FavoriteOut


async def get_favorite(id: int, db: Session = Depends(get_db)):
    favorites = db.query(Favorite).filter(Favorite.user_id == id).all()

    for fav in favorites:
        posts = db.query(Post).filter(Post.id == fav.post_id).first()
        # posts = FavoriteOut(post_querry)
        print(fav.post_id)
        print(type(posts))

    if not favorites:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")

    return posts


async def save_favorite(post_id: int, current_user: int, fav_status: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!")

    if (fav_status == 1):
        new_fav = Favorite(user_id=current_user, post_id=post_id)
        db.add(new_fav)
        db.commit()
        db.refresh(new_fav)
    else:
        fav_querry = db.query(Favorite).filter(
            Favorite.user_id == current_user, Favorite.post_id == post_id).first()
        fav_querry.delete(synchronize_session=False)
        db.commit()
    return {"message": "successfull"}
