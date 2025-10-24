from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid as PyUUID


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserSignup(UserBase):
    password: str

class UserPublic(UserBase):
    uuid: PyUUID.UUID
    is_active: bool
    is_verified: bool
    created_at: datetime
