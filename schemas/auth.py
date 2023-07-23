from typing import Optional
from pydantic import BaseModel, Field
from schemas.user import UserBase, UserSchema


class LoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class SignUpRequest(UserBase):
    pass

    class Config:
        orm_mode = True


class SignupResponse(BaseModel):
    user: UserSchema = Field(default=None)
    token: str = Field(default=None)

    class Config:
        orm_mode = True
