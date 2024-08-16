from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    category: str
    quantity: str
    price: float
    owner_id: int


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    quantity: str | None = None
    price: float | None = None


class ItemReturn(BaseModel):
    id: int
    name: str
    description: str
    category: str
    quantity: str
    price: float
    owner_id: int