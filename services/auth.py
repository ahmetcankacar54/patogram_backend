from models import User
from schemas import LoginRequest, SignUpRequest,SignupResponse
from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session
from database.configuration import get_db
from utils import hashing
from security import oauth2

async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found!")
    
    
    if not hashing.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Incorrect email or password.")
    
    access_token = oauth2.create_access_token(user)

    return {"access_token": access_token, "token_type": "bearer"}

async def signup(user: SignUpRequest, db: Session = Depends(get_db)):  
    isExist = db.query(User).filter(User.email == user.email)

    if isExist.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"An account with email already exist.")

    hashed_password = hashing.hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = oauth2.create_access_token(new_user)
    
    print(access_token)

    return SignupResponse(user= new_user.__dict__ ,token= access_token)