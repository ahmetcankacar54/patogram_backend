from models import Post
from schemas import CreatePost,PostBase
from fastapi import  Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session

async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

async def create_posts(user_id: int,post: PostBase,db: Depends(get_db)):    

    new_post = Post(**post.dict())

    new_post.owner_id = user_id

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return post

async def delete_post(id: int, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized for performed request action!")

    post_querry.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

async def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized for performed request action!")


    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()