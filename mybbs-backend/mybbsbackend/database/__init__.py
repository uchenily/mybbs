from sqlalchemy.ext import declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()
_ENGINE = None


def create_table(engine):
    Base.metadata.create_all(engine)


def get_engine():
    # return create_ENGINE(
    #     "mysql+pymysql://root:root@localhost:3306/test?charset=utf8",
    #     echo=True)
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = create_engine('sqlite://', echo=True)
        Base.metadata.create_all(_ENGINE)
    return _ENGINE


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
