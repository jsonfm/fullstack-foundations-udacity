from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def config():
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
    session = Session(engine)
    return session, Base