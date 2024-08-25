from app import db, schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from app.api.deps import get_current_user

router = APIRouter()


@router.get("/{item_id}")
async def get_by_id(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> schemas.ItemReturn:
    return crud.item.get(db=db, id=item_id, owner_id=current_user.id)


@router.get("/")
async def get_all_items(
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> Page[schemas.ItemReturn]:
    query = crud.item.get_multi_by_owner(db=db, owner_id=current_user.id)
    return paginate(query)


@router.post("/")
async def create_item(
    data: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> schemas.ItemReturn:
    data_extended = schemas.ItemCreateExtended(**data.dict(), owner_id=current_user.id)
    return crud.item.create(db=db, data=data_extended)


@router.patch("/{item_id}")
async def update_item_info(
    item_id: int,
    data: schemas.ItemUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> schemas.ItemReturn:
    return crud.item.update(db=db, id=item_id, owner_id=current_user.id, data=data)


@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> None:
    return crud.item.delete(db=db, id=item_id, owner_id=current_user.id)
