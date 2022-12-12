from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite://menusapp.db")
Base.metadata.create_all(engine)