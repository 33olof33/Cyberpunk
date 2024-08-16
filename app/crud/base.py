from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.orm import Session

_CreateType = TypeVar("_CreateType")
_UpdateType = TypeVar("_UpdateType")
_ReturnType = TypeVar("_ReturnType")


class BaseCRUD(ABC, Generic[_CreateType, _UpdateType, _ReturnType]):
    @abstractmethod
    def get(self, db: Optional[Session], *, id: int) -> Optional[_ReturnType]:
        ...

    @abstractmethod
    def get_multi(self, db: Optional[Session]) -> list[_ReturnType]:
        ...

    @abstractmethod
    def create(self, db: Optional[Session], *, data: _CreateType) -> _ReturnType:
        ...

    @abstractmethod
    def update(self, db: Optional[Session], *, id: int, data: _UpdateType) -> None:
        ...

    @abstractmethod
    def delete(self, db: Optional[Session], *, id: int) -> None:
        ...