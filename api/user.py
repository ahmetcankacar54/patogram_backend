from fastapi import Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.user import ProfileOut
from schemas.user import UpdateUserSchema
from security import oauth2
import services

router = APIRouter(prefix="/api/user", tags=["Users"])


@router.get("/get/{id}", response_model=ProfileOut)
async def get_profile(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.get_profile(id, current_user.id, db)


@router.put("/update", response_model=UpdateUserSchema)
async def update_profile(
    updated_user: UpdateUserSchema,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.update_profile(current_user.id, updated_user, db)
