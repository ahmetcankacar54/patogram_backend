from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from schemas.image import ImageBase


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    profile_image: Optional[str] = None

    class Config:
        orm_mode = True


class UpdateUserSchema(BaseModel):
    full_name: str = Field(default=None)
    email: str = Field(default=None)
    profile_image: Optional[str] = None
    user_bio: str = Field(default=None)


class UserSchema(BaseModel):
    id: int = Field(default=None)
    full_name: str = Field(default=None)
    email: str = Field(default=None)
    profile_image: Optional[str] = None
    user_bio: str = Field(default=None)

    class Config:
        orm_mode = True


class PostProfile(BaseModel):
    id: int = Field(default=None)
    images: List[ImageBase]

    class Config:
        orm_mode = True


class ProfileOut(UserSchema):
    followers: int = Field(default=None)
    isFollow: bool = Field(default=None)
    posts: List[PostProfile]

    class Config:
        orm_mode = True
