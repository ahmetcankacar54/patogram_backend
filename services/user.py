from uuid import uuid4
from models import User
from schemas import SignUpRequest
from fastapi import status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.post import ProfileOut, PostProfile
from schemas.image import ImageBase
from utils import Constants as consts
from typing import List
from utils.converting import convert_to_file


async def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()
    return users


async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")

    """postList = []

    for post in user.posts:
        print(post.image_url[0].imageUrl)
        postList.append(id=id, image_url=post.image_url[0].imageUrl)
    ProfileOut(id=user.id, full_name=user.full_name, email=user.email, profile_image=user.profile_image, posts=List[PostProfile(postList)])"""
    return user 


async def update_user(id: int, updated_user: UserSchema, db: Session = Depends(get_db)):
    user_querry = db.query(User).filter(User.id == id)
    user = user_querry.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")

    user_info = User(**updated_user.dict())

    if user_info.profile_image != "":
        newImage = user_info.profile_image
        print(f"new Image {newImage}")
        _image = convert_to_file(newImage)
        unique_id = str(uuid4().hex)
        file_name = f"{id}"+f"/profile_image"+f"/{unique_id}"+".jpg"
        consts.bucket.put_object(Key=file_name, Body=_image)
        image_url = f"https://patogram-s3.s3.amazonaws.com/"+f"{file_name}"
        print(f"Image Url {image_url}")
        user_info.profile_image = image_url
        user_querry.update(user_info, synchronize_session=False)
        db.commit()
    else:
        user_querry.update(user_info, synchronize_session=False)
        db.commit()

    return user_querry.first()
