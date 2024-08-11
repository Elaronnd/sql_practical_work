from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy import ForeignKey, String, Integer
from . import Config


class Users(Config.BASE):
    __tablename__ = "users"

    username: Mapped[str]
    password: Mapped[str]