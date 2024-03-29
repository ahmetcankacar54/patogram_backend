from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from schemas.disease import Disease
from security import oauth2
import services


router = APIRouter(prefix="/api/search", tags=["Search"])


@router.post("/mainpage/{keyword}", status_code=status.HTTP_200_OK)
async def searchMainpage(
    keyword: str, current_user: int = 1, db: Session = Depends(get_db)
):
    return await services.searchMainpage(keyword, current_user, db)


@router.post("/discover/{keyword}", status_code=status.HTTP_200_OK)
async def searchDiscover(keyword: str, db: Session = Depends(get_db)):
    return await services.searchDiscover(keyword, db)


@router.post("/sharecase/{keyword}", status_code=status.HTTP_200_OK)
async def searchOnlyDisease(keyword: str, db: Session = Depends(get_db)):
    return await services.searchOnlyDisease(keyword, db)
