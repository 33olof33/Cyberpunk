from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.db import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_username(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, hashed_pass: str):
    user = get_user_by_username(db, email)
    if not user:
        return False
    if not verify_password(hashed_pass, user.hashed_pass):
        return False
    return user
