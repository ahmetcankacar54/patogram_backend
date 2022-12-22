from db.base import Base
from db.base_class import Base
from db.session import engine
from apis.base import api_router
from core.settings import settings
from fastapi import FastAPI

app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/")
def index():
    return {"Welcome Patogram App & Semih Ibnedir"}
