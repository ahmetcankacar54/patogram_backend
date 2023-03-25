import boto3

class Constants():

    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS = 60
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Patogram54@database-1.cpkphrsvchmt.eu-central-1.rds.amazonaws.com"
    AWS_BUCKET = "patogram-s3"
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(AWS_BUCKET)   

