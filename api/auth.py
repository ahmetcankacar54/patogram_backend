from fastapi import APIRouter, Depends, status
from schemas import LoginRequest
from sqlalchemy.orm import Session
from database.configuration import  get_db
from schemas import UserOut, SignUpRequest
import services

router = APIRouter(
    prefix="/api/auth",
    tags=['Authentication'])

@router.post('/login')
async def login(request_body: LoginRequest, db: Session = Depends(get_db)):

    return await services.login(request_body, db) 
    
@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model= UserOut)
async def register(user: SignUpRequest, db: Session = Depends(get_db)):  

    return await services.register(user, db)
