from .config import Config
from sqlalchemy import select

from .models import Group, Users


def auth(username: str, password: str):
    with Config.SESSION() as session:
        session.add(Users(username=username, password=password))
        session.commit()


def login(username: str, password: str):
    with Config.SESSION() as session:
        query = select(Users).where(Users.username == username)
        user = session.scalars(query).first()
        if user is None:
            return None
        if user.password == password:
            return True
        

def delete_user(username: str, password: str):
    if login(username=username, password=password) == True:
        with Config.SESSION() as session:
            query = select(Users).where(Users.username == username)
            user = session.scalars(query).first()
            session.delete(user)
            session.commit()
            return True
    return False



# migrate()