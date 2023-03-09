from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.configuration import  get_db
from schemas import SignupResponse, SignUpRequest, Token, LoginRequest
import services

router = APIRouter(
    prefix="/api/auth",
    tags=['Authentication'])

@router.post('/login', response_model= Token)
async def login(request_body: LoginRequest, db: Session = Depends(get_db)):

    return await services.login(request_body, db) 
    
@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model= SignupResponse)
async def signup(user: SignUpRequest, db: Session = Depends(get_db)):  

    return await services.signup(user, db)
