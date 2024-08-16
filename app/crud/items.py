from pydantic.errors import EmailError
from app.crud.base import BaseCRUD
from typing import Optional
from app import schemas
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.db.items import Item



class ItemCRUD(
    BaseCRUD[schemas.ItemCreate, schemas.ItemUpdate, schemas.ItemReturn]
):
    def get(self, db: Optional[Session], *, id: int) -> Optional[schemas.ItemReturn]:
        db = self.db
        item = db.query(Item).get(id)
        return schemas.ItemReturn(**item)

    
    def get_multi(self, db: Optional[Session]) -> list[schemas.ItemReturn]:
        db = self.db
        items = db.query(Item)
        return items

    
    def create(self, db: Optional[Session], *, data: schemas.ItemCreate) -> schemas.ItemReturn:
        db = self.db
        form = jsonable_encoder(data)
        db_obj = self.model(**form)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    
    def update(self, db: Optional[Session], *, id: int, data: schemas.ItemUpdate) -> None:
        db = self.db
        item = db.query(self.model).get(id)
        form = {key: value for key, value in dict(data).items() if value is not None}
        for key, value in form.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item


    
    def delete(self, db: Optional[Session], *, id: int) -> None:
        db = self.db
        item = db.query(Item).filter(Item.id==id).first()
        db.delete(item)
        db.commit()