from models import User
from schemas import User,UserBase,CreateUser
from fastapi import status, Depends, APIRouter
from database.configuration import  get_db
from sqlalchemy.orm import Session
from typing import List
import services

router = APIRouter(
    prefix="/users",
    tags=['Kullanicilar']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= User)
async def create_user(user: UserBase, db: Session = Depends(get_db)):  

    return await services.create_user(user, db)

@router.get("/", response_model= List[User])
async def get_users(db: Session = Depends(get_db)):

    return await services.get_users(db)

@router.get("/{id}", response_model= User)
async def get_user(id: int, db: Session = Depends(get_db)):
    
    return await services.get_user(id, db)

@router.put("/{id}", response_model= User)
async def update_user(id: int, updated_user: CreateUser, db: Session = Depends(get_db)):
    
    return await services.update_user(id, updated_user, db)
