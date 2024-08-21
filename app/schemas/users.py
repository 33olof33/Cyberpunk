from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    hashed_pass: str


class UserUpdate(BaseModel):
    hashed_pass: str


class UserReturn(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
        from_attributes = True
