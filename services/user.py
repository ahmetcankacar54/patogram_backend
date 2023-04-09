from uuid import uuid4
from models import User
from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from schemas.user import UpdateUserSchema
from utils import Constants as consts
from typing import List
from utils.converting import convert_to_file


async def get_profile(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")

    return user


async def update_profile(id: int, updated_user: UpdateUserSchema, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")

    if updated_user.profile_image != "":
        newImage = updated_user.profile_image
        _image = convert_to_file(newImage)
        unique_id = str(uuid4().hex)
        file_name = f"{id}"+f"/profile_image"+f"/{unique_id}"+".jpg"
        consts.bucket.put_object(Key=file_name, Body=_image)
        image_url = f"https://patogram-s3.s3.amazonaws.com/"+f"{file_name}"
        updated_user.profile_image = image_url

    else:
        user_query.update(updated_user.dict(), synchronize_session=False)
        db.commit()

    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_query.first()
