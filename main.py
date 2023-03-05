from random import randrange
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from schemas import models, schemas
from utils import utilities
from db.database import engine, SessionLocal, get_db
from routers import posts, users, auth



models.Base.metadata.create_all(bind=engine)




while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Cerrah54', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection Succesfull!")
        break
    except Exception as error:
        print("Cannot connect the Database!")
        print("ERROR: ", error)
        time.sleep(2)

app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": " Hello There!."}


# USER REQUESTS ...
