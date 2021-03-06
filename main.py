from typing import Optional

from fastapi import FastAPI

from datetime import datetime, timedelta
from typing import List, Optional
from pprint import pprint

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    or_,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session


app = FastAPI()


@app.get("/", summary="Get a hello world json")
def hello(
    name: str = "World",
):
    """
    Hello world view
    1. processes `request`
    1. returns greeting
    """
    return {"Hello": name}

@app.get("/search/{sstring}")
def ssearch(sstring):
    qq: str = get_books(sstring)
    return {"search": qq}




engine = create_engine("sqlite:///lib.sqlite", echo=True)

Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class Book(Base):
    __tablename__ = "books"

    file = Column(String(32), primary_key=True)
    title = Column(String(512))
    genres = Column(String(32))
    last_name = Column(String(32))
    first_name = Column(String(32))
    lang = Column(String(32))
    opt = Column(String(32))

    def __str__(self):
        return (
#            f"{self.__class__.__name__}(file={self.file!r}, "
            f"(file={self.file!r}, "
            f"title={self.title!r}, "
            f"genres={self.genres!r}, "
            f"last_name={self.last_name!r}, "
            f"first_name={self.first_name!r}, "
            f"lang={self.lang!r}, "
            f"opt={self.opt!r})"
        )

    def __repr__(self):
        return str(self)

def get_books(search_in):
    search = "%{}%".format(search_in)
    session = Session()
    booklist: List[Book] = session.query(Book).filter(or_(Book.title.like(search), Book.first_name.like(search), Book.last_name.like(search))).all()
    session.close()
    pprint(booklist)
    return (booklist)

