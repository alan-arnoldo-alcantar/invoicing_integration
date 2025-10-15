from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserSignup(UserBase):
    password: str

class UserPublic(UserBase):
    uuid: str
    is_active: bool
    is_verified: bool
    created_at: datetime
