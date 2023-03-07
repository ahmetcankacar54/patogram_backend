from typing import Optional
from pydantic import BaseModel,Field
from schemas.user import UserBase,UserSchema


class LoginRequest(BaseModel): 
    email: str
    password: str

class Token(BaseModel):
    access_token: str = Field(default=None)
    token_type: str = Field(default=None)

class TokenData(BaseModel):
    id: Optional[str] = None

class SignUpRequest(UserBase):
    pass

class SignupResponse(BaseModel):
    user: UserSchema = Field(default=None)
    token: str = Field(default=None)

    class Config:
        orm_mode = True
