from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.orm import Session

_CreateType = TypeVar("_CreateType")
_UpdateType = TypeVar("_UpdateType")
_ReturnType = TypeVar("_ReturnType")


class BaseCRUD(ABC, Generic[_CreateType, _UpdateType, _ReturnType]):
    @abstractmethod
    def get(self, db: Session, *, id: int) -> Optional[_ReturnType]:
        ...

    @abstractmethod
    def get_multi(self, db: Session, skip: int = 0, limit: int = 10) -> List[_ReturnType]:
        ...

    @abstractmethod
    def create(self, db: Session, *, data: _CreateType) -> _ReturnType:
        ...

    @abstractmethod
    def update(self, db: Session, *, id: int, data: _UpdateType) -> Optional[_ReturnType]:
        ...

    @abstractmethod
    def delete(self, db: Session, *, id: int) -> Optional[_ReturnType]:
        ...