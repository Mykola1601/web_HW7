
from sqlalchemy.exc import SQLAlchemyError
from db import session
from models import User

if __name__ == "__main__":
    login = input ("login:>>>")
    password = input("pass:>>>")
    try:
        user = User(login = login, password = password)
        session.add(user)
        session.commit()
    except SQLAlchemyError as e :
        session.rollback()
        print(e)
    finally:
         session.close()