from app.crud.base import BaseCRUD
from typing import Optional
from app import schemas
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.db import users


from app.db.users import User


class UserCRUD(BaseCRUD[schemas.UserCreate, schemas.UserUpdate, schemas.UserReturn]):
    def get(self, db: Optional[Session], *, id: int) -> Optional[schemas.UserReturn]:
        user = db.query(User).get(id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = jsonable_encoder(user)
        return schemas.UserReturn(**user_data)

    def get_multi(self, db: Optional[Session]) -> list[schemas.UserReturn]:
        users = db.query(User).all()
        return [schemas.UserReturn.from_orm(user) for user in users]

    def create(
        self, db: Optional[Session], *, data: schemas.UserCreate
    ) -> schemas.UserReturn:
        db_obj = User(**data.dict())
        db.add(db_obj)
        try:
            db.commit()
            db.refresh(db_obj)
            return schemas.UserReturn.from_orm(db_obj)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400, detail="User with this email already exists."
            )

    def update(
        self, db: Optional[Session], *, id: int, data: schemas.UserUpdate
    ) -> None:
        user = db.query(User).get(id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return schemas.UserReturn.from_orm(user)

    def delete(self, db: Optional[Session], *, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
