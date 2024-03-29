from fastapi import FastAPI
from models import Base
from database.configuration import engine
from api import (
    case_follow,
    post,
    user,
    auth,
    like,
    comment,
    favorite,
    poll,
    vote,
    user_follow,
    search,
)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(like.router)
app.include_router(comment.router)
app.include_router(favorite.router)
app.include_router(poll.router)
app.include_router(vote.router)
app.include_router(case_follow.router)
app.include_router(user_follow.router)
app.include_router(search.router)


@app.get("/")
def root():
    return {"message": "Patogram Project, Check For AWS"}
