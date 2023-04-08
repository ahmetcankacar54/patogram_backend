from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    profile_image: Optional[str] = None


class UserSchema(BaseModel):
    id: int = Field(default=None)
    full_name: str = Field(default=None)
    email: str = Field(default=None)
    profile_image: Optional[str] = None
    user_bio: str = Field(default=None)

    class Config:
        orm_mode = True
