from app import db, schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.deps import get_current_user

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
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> schemas.UserReturn:
    return crud.user.update(db=db, owner_id=current_user.id, data=data, id=user_id)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserReturn = Depends(get_current_user),
) -> None:
    return crud.user.delete(db=db, owner_id=current_user.id, id=user_id)
