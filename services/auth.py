from models import User
from schemas import LoginRequest, SignUpRequest
from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session
from database.configuration import get_db
from utils import hashing
from security import oauth2

async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials!")
    
    
    if not hashing.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

async def register(user: SignUpRequest, db: Session = Depends(get_db)):  

    hashed_password = hashing.hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user