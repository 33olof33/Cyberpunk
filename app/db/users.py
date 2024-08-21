from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_pass = Column(String)
