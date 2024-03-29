from uuid import uuid4
from models import User
from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from models.user_follow import UserFollow
from schemas.user import UpdateUserSchema
from utils import Constants as consts
from utils.converting import convert_to_file


async def get_profile(id: int, currentUser: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!"
        )

    user.followers = db.query(UserFollow).filter(UserFollow.follows_id == id).count()
    isFollowRequest = (
        db.query(UserFollow)
        .filter(UserFollow.user_id == currentUser, UserFollow.follows_id == id)
        .first()
    )
    print(isFollowRequest)

    if isFollowRequest:
        user.isFollow = True
    else:
        user.isFollow = False

    user.password = ""

    return user


async def update_profile(
    id: int, updated_user: UpdateUserSchema, db: Session = Depends(get_db)
):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!"
        )

    if updated_user.profile_image != "":
        newImage = updated_user.profile_image
        _image, thumb = convert_to_file(newImage)
        unique_id = str(uuid4().hex)
        file_name = f"{id}" + f"/profile_image" + f"/{unique_id}" + ".jpg"
        consts.bucket.put_object(Key=file_name, Body=_image)
        image_url = f"https://patogram-s3.s3.amazonaws.com/" + f"{file_name}"
        updated_user.profile_image = image_url

    else:
        user_query.update(updated_user.dict(), synchronize_session=False)
        db.commit()

    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return updated_user
