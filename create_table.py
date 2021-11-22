from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)

engine = create_engine("sqlite:///lib.sqlite", echo=True)


metadata = MetaData()

users_table = Table(
    "books",
    metadata,
    Column("file", String(32)),
    Column("title", String(512)),
    Column("genres", String(32)),
    Column("last_name", String(32)),
    Column("first_name", String(32)),
    Column("lang", String(32)),
    Column("opt", String(32)),
)


if __name__ == "__main__":
    metadata.create_all(engine)
