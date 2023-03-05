from models import Post
from schemas import Post,CreatePost
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['Postlar']
)

@router.get("/", response_model= List[Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= Post)
def create_posts(post: CreatePost, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    # (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

@router.get("/{id}", response_model= Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()

    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return post

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    deleted_post = db.query(Post).filter(Post.id == id)


    if deleted_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= Post)
def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *  """, (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    

    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()
