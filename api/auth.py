from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from database.configuration import  get_db
import services

router = APIRouter(
    prefix="/api/auth",
    tags=['Authentication'])

@router.post('/login')
async def login(request_body: HTTPBasicCredentials = Depends(), db: Session = Depends(get_db)):

    return await services.login(request_body, db) 

@router.post("/register")
async def register():
    return {
        "message": "Success"
    }
    
