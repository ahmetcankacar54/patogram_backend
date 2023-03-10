from models import Post
from schemas import CreatePost
from fastapi import  Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from security import oauth2

async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(Post).all()
    return posts

async def create_posts(post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = Post(owner_id= current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

async def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return post

async def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized for performed request action!")

    post_querry.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

async def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized for performed request action!")


    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()