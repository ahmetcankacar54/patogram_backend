import sys
sys.path.append("..")
from schemas import models, schemas
from utils import utilities
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from db.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/users",
    tags=['Kullanicilar']
)


def find_index_user(id):
    for i, p in enumerate(models.User):
        if p['id'] == id:
            return i


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):  

    hashed_password = utilities.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model= List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model= schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return user

@router.put("/{id}", response_model= schemas.User)
def update_user(id: int, updated_user: schemas.CreateUser, db: Session = Depends(get_db)):
    user_querry = db.query(models.User).filter(models.User.id == id)
    user = user_querry.first()

    if user == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    

    user_querry.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_querry.first()

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    deleted_user = db.query(models.User).filter(models.User.id == id)


    if deleted_user == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    deleted_user.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)