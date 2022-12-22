from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.crud.users import create_new_user,get_all_users
from db.session import get_db

from schemas.users import CreateUser,ShowUser

router = APIRouter()

@router.post("/",response_model=ShowUser)
def create_user(user:CreateUser,db:Session=Depends(get_db)):
    user = create_new_user(user,db)
    return user

@router.get("/get-all-user",response_model=List[ShowUser])
def get_all(db:Session=Depends(get_db)):
    users = get_all_users(db=db)
    return users
