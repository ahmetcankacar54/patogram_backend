from io import BytesIO
import io
from uuid import uuid4
from schemas import PostOut, CreatePost
from fastapi import  Body, File, HTTPException, UploadFile, status, Depends, APIRouter
from database.configuration import get_db
from sqlalchemy.orm import Session
from typing import List
import services, magic, boto3
from security import oauth2
from loguru import logger
from PIL import Image
import base64

router = APIRouter(
    prefix="/api/posts",
    tags=['Posts']
)

@router.get("/get", response_model= List[PostOut])
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    return await services.get_posts(db)

@router.get("/get/{id}", response_model= PostOut)
async def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_post(id, db)   

@router.get("/user/{id}", response_model= List[PostOut])
async def get_user_posts(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.get_user_posts(id, db)   

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model= PostOut)
async def create_posts(post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.id)
    return await services.create_posts(current_user.id, post, db)

@router.delete("/delete/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    return await services.delete_post(current_user.id, id, db)

@router.put("/update/{id}", response_model= PostOut)
async def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    return await services.update_post(current_user.id, id, updated_post, db)

SUPPORTED_FILE_TYPES = {
    "image/jpg":  "jpg",
    "image/jpeg": "jpg",
    "image/png": "png"
}

AWS_BUCKET = "patogram-bucket"

s3 = boto3.resource("s3")
bucket = s3.Bucket(AWS_BUCKET)
"""
async def s3_upload(contents: bytes, key: str):
    logger.info(f"uploading file")
    bucket.put_object(Key= key, Body= contents)"""

# Convert Image to Base64 
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str

# Convert Base64 to Image
def b64_2_img(data):
    buff = BytesIO(base64.b64decode(data))
    return Image.open(buff)


def convert_to_file(bs64File):

    if bs64File:
        try:
            if 'base64' in bs64File:
                format, imgstr = bs64File.split(';base64,')
            else:
                imgstr = bs64File
            
            decoded_image = Image.open(BytesIO(base64.b64decode(imgstr)))
            output_image = BytesIO()
            # convert
            if decoded_image.mode in ("RGBA", "P"): 
                    decoded_image = decoded_image.convert("RGB") 
            
            decoded_image.save(output_image, format="JPEG", quality=40)
            output_image.seek(0)

            return output_image
        except Exception as e:
            print(str(e))
        finally:
            decoded_image.close()
            imgstr.file.close()
            


@router.post("/upload")
async def upload(files: List[UploadFile] = File(...), current_user: int = Depends(oauth2.get_current_user)):
        for file in files:
            try:
                _image = convert_to_file(file)
                unique_id = str(uuid4().hex)
                file_name = f"{current_user.id}/"+f"{unique_id}"+".jpg"
                print(file_name)
                
                bucket.put_object(Key = file_name, Body = _image)
            except Exception:
                raise HTTPException(status_code=500, detail='Something went wrong')
        return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}  
    
    
    
    
    
    
    
    
    
    
    
"""    if not files:
        print("hata!")
        #raise HTTPException
    
    for file in files:
        contents = await file.read()

    file_type = magic.from_buffer(buffer=contents, mime=True)
    if file_type not in SUPPORTED_FILE_TYPES:
        print("hata 2")

    await s3_upload(contents=contents, key=f"{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}")"""