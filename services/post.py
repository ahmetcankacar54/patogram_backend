from uuid import uuid4
from models import Post, Image
from schemas import CreatePost, PostBase, ImageBase
from fastapi import Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from utils import convert_to_file
from utils import Constants as consts
from typing import List


async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!")
    return post


async def get_user_posts(id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.owner_id == id).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!")
    return posts


async def create_posts(user_id: int, post: PostBase, images: List[ImageBase], db: Depends(get_db)):

    new_post = Post(**post.dict())
    new_post.owner_id = user_id

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    post_id = new_post.id

    for im in images:

        try:
            newImage = Image(**im.dict())
            _image, thmbnail = convert_to_file(im.image)
            unique_id = str(uuid4().hex)
            file_name = f"{user_id}"+f"/{post_id}"+f"/{unique_id}"+".jpg"
            thmb_name = f"{user_id}"+f"/{post_id}" + \
                "/thumbnail"+f"/{unique_id}"+".jpg"
            consts.bucket.put_object(Key=thmb_name, Body=thmbnail)
            consts.bucket.put_object(Key=file_name, Body=_image)
            thumbnail = f"https://patogram-s3.s3.amazonaws.com/"+f"{thmb_name}"
            image_url = f"https://patogram-s3.s3.amazonaws.com/"+f"{file_name}"
            print(f"Image Url {image_url}")
            newImage.thumbnail = thumbnail
            newImage.image = image_url
            newImage.post_id = post_id
            db.add(newImage)
            db.commit()
            db.refresh(newImage)
        except Exception:
            raise HTTPException(status_code=500, detail='Something went wrong')
        # return {"message": "Successfuly uploaded"}

    return new_post


async def delete_post(user_id: int, id: int, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!")

    if post.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Post does not belong current user!")

    post_querry.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def update_post(user_id: int, id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!")

    if post.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Post does not belong current user!")

    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()
