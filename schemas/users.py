from pydantic import BaseModel,EmailStr

class CreateUser(BaseModel):
    name:str
    lastname:str
    email:EmailStr
    password: str

class ShowUser(BaseModel):
    name:str
    lastname:str
    email:EmailStr

    class Config():
        orm_mode = True