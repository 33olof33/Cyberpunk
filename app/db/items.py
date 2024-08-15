from sqlalchemy import Column, String, Integer, Float


class Item():
    __tablename__="item"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)