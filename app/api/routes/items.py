from app import db, schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter()


@router.get("/{item_id}")
async def get_by_id(
    item_id: int,
    db: Session = Depends(get_db),
) -> schemas.ItemReturn:
    return crud.item.get(db=db, id=item_id)


@router.get("/")
async def get_all_items(
    db: Session = Depends(get_db),
) -> Page[schemas.ItemReturn]:
    query = crud.item.get_multi(db=db)
    return paginate(query)


@router.post("/")
async def create_item(
    data: schemas.ItemCreate,
    db: Session = Depends(get_db),
) -> schemas.ItemReturn:
    return crud.item.create(db=db, data=data)


@router.patch("/{item_id}")
async def update_item_info(
    item_id: int,
    data: schemas.ItemUpdate,
    db: Session = Depends(get_db),
) -> schemas.ItemReturn:
    return crud.item.update(db=db, data=data, id=item_id)


@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
) -> None:
    return crud.item.delete(db=db, id=item_id)
