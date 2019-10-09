from sqlalchemy.ext import declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()
# _URL = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
# create database in memory, it's highly recommanded during development.
_URL = 'sqlite://'
_ENGINE = None


def create_table(engine):
    Base.metadata.create_all(engine)


def get_engine():
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = create_engine(_URL, echo=True)
        create_table(_ENGINE)
    return _ENGINE


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
