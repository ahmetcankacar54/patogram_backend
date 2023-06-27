from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database.configuration import get_db
from schemas.disease import Disease
from security import oauth2
import services


router = APIRouter(prefix="/api/search", tags=["Search"])


@router.post("/{keyword}]", status_code=status.HTTP_200_OK)
async def search(keyword: str, db: Session = Depends(get_db)):
    return await services.search(keyword, db)
