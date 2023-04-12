from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.favorite import FavoriteOut
from schemas.post import PostOut
from security import oauth2
import services

router = APIRouter(
    prefix="/api/favorite",
    tags=['Favorite']
)


@router.get("/get/{id}", response_model=List[PostOut])
async def get_favorite(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_favorite(id, db)


@router.post("/{post_id}/{fav_status}", status_code=status.HTTP_200_OK)
async def save_favorite(post_id: int, fav_status: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.save_favorite(post_id, current_user.id, fav_status, db)
