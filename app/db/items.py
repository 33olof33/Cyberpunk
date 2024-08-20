from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    # owner_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    # owner = relationship("users", foreign_keys=[owner_id])
