from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(
        Integer, 
        primary_key = True
    )
    name = Column(
        String(80),
        nullable=False
    )



class MenuItem(Base):
    __tablename__ = 'menuitems'
    id = Column(
        Integer, 
        primary_key = True
    )
    course = Column(
        String(250)
    )
    description = Column(
        String(250)
    )
    price = Column(
        String(8)
    )
    restaurant_id = Column(
        Integer,
        ForeignKey('restaurant.id')
    )
    restaurant = relationship(Restaurant)
