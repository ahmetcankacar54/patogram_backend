from schemas import PostOut, CreatePost, CreatePostImageModel
from fastapi import status, Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.poll import PollCreate
from schemas.post import DiscoverOut
import services
from security import oauth2

router = APIRouter(prefix="/api/posts", tags=["Posts"])


@router.get("/get/mainpage", response_model=List[PostOut])
async def get_posts_mainpage(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    return await services.get_posts_mainpage(current_user.id, db)


@router.get("/get/discover", response_model=List[DiscoverOut])
async def get_posts_discover(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.get_posts_discover(current_user.id, db)


@router.get("/get/{id}", response_model=PostOut)
async def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.get_post(id, current_user.id, db)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_posts(
    post: CreatePost,
    images: List[CreatePostImageModel],
    poll: List[PollCreate],
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.create_posts(current_user.id, post, images, poll, db)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.delete_post(current_user.id, id, db)


@router.put("/update/{id}", response_model=PostOut)
async def update_post(
    id: int,
    updated_post: CreatePost,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return await services.update_post(current_user.id, id, updated_post, db)
