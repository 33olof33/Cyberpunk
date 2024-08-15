from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    category: str
    quantity: str
    price: float


class ItemUpdate(BaseModel):
    name: str
    description: str
    category: str
    quantity: str
    price: float


class ItemReturn(BaseModel):
    id: int
    name: str
    description: str
    category: str
    quantity: str
    price: float