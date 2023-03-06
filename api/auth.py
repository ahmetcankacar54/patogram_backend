from fastapi import APIRouter, Depends
from schemas import LoginRequest
from sqlalchemy.orm import Session
from database.configuration import  get_db
import services

router = APIRouter(
    prefix="/api/auth",
    tags=['Authentication'])

@router.post('/login')
async def login(request_body: LoginRequest, db: Session = Depends(get_db)):

    return await services.login(request_body, db) 

@router.post("/signup")
async def register():
    return {
        "message": "Success"
    }
    
