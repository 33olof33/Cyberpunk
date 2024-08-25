from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.items import Item
from app.db.users import User
from .base import Base


DATABASE_URL = "postgresql://postgres:admin@postgres:5432/test"

engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
