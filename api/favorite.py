from fastapi import Depends, APIRouter, status
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.favorite import SetFavoriteBase, PostFavorite
from security import oauth2
import services

router = APIRouter(
    prefix="/api/favorite",
    tags=['Favorite']
)


@router.get("/get", response_model=List[PostFavorite])
async def get_favorite(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_favorite(current_user.id, db)


@router.post("/set", status_code=status.HTTP_200_OK)
async def set_favorite(favorite: SetFavoriteBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.set_favorite(favorite, current_user.id, db)
