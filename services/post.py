from uuid import uuid4

from models import Post, Image
from models.favorite import Favorite
from models.case_follow import Follow
from models.poll import Poll
from models.user_follow import UserFollow
from schemas import CreatePost, CreatePostImageModel
from fastapi import Response, status, HTTPException, Depends
from database.configuration import get_db
from sqlalchemy.orm import Session
from schemas.poll import PollCreate
from utils import convert_to_file
from utils import Constants as consts
from typing import List


async def get_posts_mainpage(id: int, db: Session = Depends(get_db)):
    follows_querry = db.query(UserFollow).filter(UserFollow.user_id == id).all()
    postList = []

    for ids in follows_querry:
        oneUserPostsQuerry = (
            db.query(Post).filter(Post.owner_id == ids.follows_id).all()
        )

        for post in oneUserPostsQuerry:
            favoriteCheckedPost = favoriteCheck(id, post, db)
            followFavoriteCheckedPost = followCheck(id, favoriteCheckedPost, db)
            postList.append(followFavoriteCheckedPost)

    return postList


async def get_posts_discover(id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    post_list = []

    for p in posts:
        favoriteCheckedPost = favoriteCheck(id, p, db)
        followFavoriteCheckedPost = followCheck(id, favoriteCheckedPost, db)
        post_list.append(followFavoriteCheckedPost)

    return post_list


async def create_posts(
    user_id: int,
    post: CreatePost,
    images: List[CreatePostImageModel],
    polls: List[PollCreate],
    db: Depends(get_db),
):
    new_post = Post(**post.dict())
    new_post.owner_id = user_id

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    post_id = new_post.id

    for pol in polls:
        poll = Poll(**pol.dict())
        poll.user_id = user_id
        poll.post_id = post_id
        poll.item = pol.item
        db.add(poll)
        db.commit()
        db.refresh(poll)

    for im in images:
        try:
            newImage = Image(**im.dict())
            _image, thmbnail = convert_to_file(im.image)
            unique_id = str(uuid4().hex)
            file_name = f"{user_id}" + f"/{post_id}" + f"/{unique_id}" + ".jpg"
            thmb_name = (
                f"{user_id}" + f"/{post_id}" + "/thumbnail" + f"/{unique_id}" + ".jpg"
            )
            consts.bucket.put_object(Key=thmb_name, Body=thmbnail)
            consts.bucket.put_object(Key=file_name, Body=_image)
            thumbnail = f"https://patogram-s3.s3.amazonaws.com/" + f"{thmb_name}"
            image_url = f"https://patogram-s3.s3.amazonaws.com/" + f"{file_name}"
            newImage.thumbnail = thumbnail
            newImage.image = image_url
            newImage.post_id = post_id
            newImage.zoom_amount = im.zoom_amount
            newImage.paint_type = im.paint_type
            db.add(newImage)
            db.commit()
            db.refresh(newImage)
        except Exception:
            raise HTTPException(status_code=500, detail="Something went wrong")
        # return {"message": "Successfuly uploaded"}

    return new_post


async def delete_post(user_id: int, id: int, db: Session = Depends(get_db)):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!"
        )

    if post.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Post does not belong current user!",
        )

    post_querry.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def update_post(
    user_id: int, id: int, updated_post: CreatePost, db: Session = Depends(get_db)
):
    post_querry = db.query(Post).filter(Post.id == id)
    post = post_querry.first()
    user_id = int(user_id)

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found!"
        )

    if post.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Post does not belong current user!",
        )

    post_querry.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_querry.first()


# SOME INNER FUNCTIONS DEFINED BELOW #


def favoriteCheck(id: int, post: Post, db: Session = Depends(get_db)):
    favorite_querry = (
        db.query(Favorite)
        .filter(
            Favorite.post_id == post.id,
            Favorite.user_id == id,
            Favorite.isFavorite == True,
        )
        .first()
    )
    if favorite_querry:
        post.isFavorite = True
    else:
        post.isFavorite = False

    return post


def followCheck(id: int, post: Post, db: Session = Depends(get_db)):
    follow_querry = (
        db.query(Follow)
        .filter(
            Follow.post_id == post.id, Follow.user_id == id, Follow.isFollow == True
        )
        .first()
    )
    if follow_querry:
        post.isFollow = True
    else:
        post.isFollow = False

    return post
