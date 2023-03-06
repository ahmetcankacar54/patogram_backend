from fastapi import FastAPI
from models import Base
from database.configuration import engine
from api import post, user, auth


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": " AWS Code Deploy Duzgun Bir Sekilde Calisiyor!."}

