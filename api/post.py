from schemas import PostOut, CreatePost, ImageBase
from fastapi import status, Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
import services
from security import oauth2

router = APIRouter(
    prefix="/api/posts",
    tags=['Posts']
)


@router.get("/get", response_model=List[PostOut])
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_posts(current_user.id, db)


@router.get("/get/{id}", response_model=PostOut)
async def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_post(id, current_user.id, db)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_posts(post: CreatePost, images: List[ImageBase], db: Session = Depends(get_db)):

    return await services.create_posts(1, post, images, db)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.delete_post(current_user.id, id, db)


@router.put("/update/{id}", response_model=PostOut)
async def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.update_post(current_user.id, id, updated_post, db)
