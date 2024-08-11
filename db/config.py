from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, 
                            declarative_base, 
                            DeclarativeBase, 
                            Mapped, 
                            mapped_column)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Config:
    ENGINE = create_engine("sqlite:///my_db.db", echo=True)
    BASE = declarative_base()
    BASE = Base
    SESSION = sessionmaker(bind=ENGINE)


    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)


    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)
        