from uuid import uuid4
from models import Post, Image
from schemas import CreatePost, PostBase, ImageBase
from fastapi import  Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from utils import convert_to_file
from utils import Constants as consts


async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return post

async def get_user_posts(id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.owner_id == id).all()

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return posts

async def create_posts(user_id: int, post: PostBase, bs64Texts: ImageBase, db: Depends(get_db)):    

    new_post = Post(**post.dict())

    new_post.owner_id = user_id

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    post_id = new_post.id
    img_url = Image(**bs64Texts.dict())

    for file in bs64Texts:
            try:
                _image = convert_to_file(file)
                unique_id = str(uuid4().hex)
                file_name = f"{user_id}"+f"/{post_id}"+f"/{unique_id}"+".jpg"                
                consts.bucket.put_object(Key = file_name, Body = _image)
                image_url = f"https://patogram-bucket.s3.amazonaws.com/{user_id}"+f"/{post_id}"+f"/{file_name}"
                img_url.imageUrl = image_url
                img_url.post_id = post_id
                db.add(img_url)
                db.commit()
                db.refresh(img_url)
            except Exception:
                raise HTTPException(status_code=500, detail='Something went wrong')
        #return {"message": "Successfuly uploaded"}
    
    return new_post


async def delete_post(user_id: int, id: int, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    if post.owner_id != user_id:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"Post with id: {id} does not belong current user!")

    post_querry.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

async def update_post(user_id: int ,id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    if post.owner_id != user_id:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"Post with id: {id} does not belong current user!")

    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()