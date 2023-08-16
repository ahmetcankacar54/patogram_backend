import boto3
import os
from dotenv import load_dotenv

load_dotenv()


class Constants:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
    AWS_BUCKET = os.getenv("AWS_BUCKET")

    ACCESS_TOKEN_EXPIRE_DAYS = 1
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(AWS_BUCKET)
    size = 480, 360
