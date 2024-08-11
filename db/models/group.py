from sqlalchemy.orm import Mapped, mapped_column
from ..config import Config


class Group(Config.BASE):
    __tablename__ = "groups"

    name: Mapped[str]