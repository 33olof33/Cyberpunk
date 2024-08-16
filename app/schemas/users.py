from lib2to3.pytree import Base
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    password: str


class UserReturn(BaseModel):
    id: int
    email: str