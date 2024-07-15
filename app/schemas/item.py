from pydantic import BaseModel



class ItemCreate(BaseModel):
    item_name: str
    description: str
    category: str
    quantity: int
    price: float


class ItemCreateExtended(ItemCreate):
    owner_id: int


class ItemUpdate(BaseModel):
    item_name: str
    description: str
    category: str
    quantity: int
    price: float


class TaskReturn(BaseModel):
    id: int
    item_name: str
    description: str
    category: str
    quantity: int
    price: float
    owner_id: int

class Config:
    orm_mode = True