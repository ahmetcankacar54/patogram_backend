from models import User
from schemas import User,UserBase,CreateUser
from utils import hashing
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from database.configuration import  get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/users",
    tags=['Kullanicilar']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= User)
def create_user(user: UserBase, db: Session = Depends(get_db)):  

    hashed_password = hashing.hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model= List[User])
def get_users(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    users = db.query(User).all()
    return users

@router.get("/{id}", response_model= User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return user

@router.put("/{id}", response_model= User)
def update_user(id: int, updated_user: CreateUser, db: Session = Depends(get_db)):
    user_querry = db.query(User).filter(User.id == id)
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
    
    deleted_user = db.query(User).filter(User.id == id)


    if deleted_user == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    
    deleted_user.delete(synchronize_session=False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)