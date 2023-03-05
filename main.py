from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from models import Base
from database.configuration import engine
from api import post, user, auth


Base.metadata.create_all(bind=engine)

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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": " Hello There!."}

