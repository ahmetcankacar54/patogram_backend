from models import Post
from schemas import Post,CreatePost
from fastapi import  status, Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
import services

router = APIRouter(
    prefix="/api/post",
    tags=['Posts']
)

@router.get("/get", response_model= List[Post])
async def get_posts(db: Session = Depends(get_db)):
    
    return await services.get_posts(db)
    

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model= Post)
async def create_posts(post: CreatePost, db: Session = Depends(get_db)):
    
    return await services.create_posts(post, db)

@router.get("/get/{id}", response_model= Post)
async def get_post(id: int, db: Session = Depends(get_db)):

    return await services.get_post(id, db)

@router.delete("/delete/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):

    return await services.delete_post(id, db)

@router.put("/update/{id}", response_model= Post)
async def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    
    return await services.update_post(id, updated_post, db)
