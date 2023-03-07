from pydantic import BaseModel, EmailStr,Field

class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    password: str
class UserSchema(BaseModel):
    id: int = Field(default=None)
    full_name: str = Field(default=None)
    email: str = Field(default=None)