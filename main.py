from app import app
from db import Config, login, auth, delete_user

if __name__ == "__main__":
    try:
        Config.up()
        user_data = {"username":"test2", 
                     "password":"test"}
        auth(**user_data)
        login(**user_data)
        delete_user(**user_data)
        app.run(
            host="localhost",
            port=5001,
            debug=True,
        )
    finally:
        Config.down()