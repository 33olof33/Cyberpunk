from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from app.db.session import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    owner_id = Column(Integer, ForeignKey('users.id'))