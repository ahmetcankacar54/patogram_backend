from models import User
from schemas import SignUpRequest
from fastapi import status, HTTPException, Depends
from database.configuration import  get_db
from sqlalchemy.orm import Session



async def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()
    return users

async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    return user

async def update_user(id: int, updated_user: SignUpRequest, db: Session = Depends(get_db)):
    user_querry = db.query(User).filter(User.id == id)
    user = user_querry.first()

    if user == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
    

    user_querry.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_querry.first()