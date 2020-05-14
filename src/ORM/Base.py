from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///src/ORM/kantin-itk.db')

_SessionFactory = sessionmaker(bind=engine)


def SessionFactory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
