from schemas import SignupResponse, SignUpRequest
from fastapi import Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.user import UserSchema
import services

router = APIRouter(
    prefix="/api/user",
    tags=['Users']
)


@router.get("/get", response_model=List[UserSchema])
async def get_users(db: Session = Depends(get_db)):

    return await services.get_users(db)


@router.get("/get/{id}", response_model=UserSchema)
async def get_user(id: int, db: Session = Depends(get_db)):

    return await services.get_user(id, db)


@router.put("/update/{id}", response_model=UserSchema)
async def update_user(id: int, updated_user: UserSchema, db: Session = Depends(get_db)):

    return await services.update_user(id, updated_user, db)
