from app.crud.base import BaseCRUD
from typing import Optional
from app import schemas
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


from app.db.items import Item


class ItemCRUD(BaseCRUD[schemas.ItemCreate, schemas.ItemUpdate, schemas.ItemReturn]):
    def get(
        self, db: Optional[Session], *, id: int, owner_id: int
    ) -> Optional[schemas.ItemReturn]:
        item = db.query(Item).filter(Item.owner_id == owner_id, Item.id == id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        item_data = jsonable_encoder(item)
        return schemas.ItemReturn(**item_data)

    def get_multi(self, db: Optional[Session]) -> list[schemas.ItemReturn]:
        items = db.query(Item).all()
        return items

    def get_multi_by_owner(
        self, db: Optional[Session], *, owner_id: int
    ) -> list[schemas.ItemReturn]:
        items = db.query(Item).filter(Item.owner_id == owner_id).all()
        return items

    def create(
        self, db: Optional[Session], *, data: schemas.ItemCreate
    ) -> schemas.ItemReturn:
        form = jsonable_encoder(data)
        db_obj = Item(**form)
        db.add(db_obj)
        try:
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400, detail="Item with this name already exists."
            )

    def update(
        self, db: Optional[Session], *, id: int, owner_id: int, data: schemas.ItemUpdate
    ) -> None:
        item = db.query(Item).filter(Item.id == id, Item.owner_id == owner_id).first()

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        form = {key: value for key, value in dict(data).items() if value is not None}
        for key, value in form.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    def delete(self, db: Optional[Session], *, id: int, owner_id: int) -> None:
        item = db.query(Item).filter(Item.id == id, Item.owner_id == owner_id).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(item)
        db.commit()
