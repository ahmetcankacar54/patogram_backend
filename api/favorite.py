from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.favorite import FavoriteBase, PostFavorite
from security import oauth2
import services

router = APIRouter(
    prefix="/api/favorite",
    tags=['Favorite']
)


@router.get("/get/{id}", response_model=List[PostFavorite])
async def get_favorite(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_favorite(id, db)


@router.post("/save", status_code=status.HTTP_200_OK)
async def save_favorite(favorite: FavoriteBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.save_favorite(favorite, current_user.id, db)
