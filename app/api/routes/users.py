from app import db, schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter()


@router.get("/{user_id}")
async def get_by_id(
    user_id: int,
    db: Session = Depends(get_db),
) -> schemas.UserReturn:
    return crud.user.get(db=db, id=user_id)


@router.get("/")
async def get_all_users(
    db: Session = Depends(get_db),
) -> list[schemas.UserReturn]:
    query = crud.user.get_multi(db=db)
    return query


@router.post("/")
async def create_user(
    data: schemas.UserCreate,
    db: Session = Depends(get_db),
) -> schemas.UserReturn:
    return crud.user.create(db=db, data=data)


@router.patch("/{user_id}")
async def update_user_info(
    user_id: int,
    data: schemas.UserUpdate,
    db: Session = Depends(get_db),
) -> schemas.UserReturn:
    return crud.user.update(db=db, data=data, id=user_id)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
) -> None:
    return crud.user.delete(db=db, id=user_id)
