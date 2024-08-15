from sqlalchemy import Column, Integer, String


class User():
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_pass = Column(String)