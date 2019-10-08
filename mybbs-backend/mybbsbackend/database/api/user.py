from sqlalchemy.orm import exc

from mybbsbackend import database
from mybbsbackend.database.model import user as model_user


class User:
    def get_one_by_username(self, username):
        session = database.get_session()
        query = session.query(
            model_user.UserModel).filter_by(username=username)
        try:
            user = query.one()
            return user
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_user.UserModel)
        try:
            users = query.all()
            return users
        except exc.NoResultFound:
            return None

    def add_one(self, user):
        session = database.get_session()
        try:
            session.add(user)
            session.flush()
            session.commit()
            print('#####', user)
            return user
        except Exception:
            pass
            # TODO

    def update_user(self, user):
        session = database.get_session()
        query = session.query(user.UserModel).filter_by(username=user.username)
        try:
            query.update(user)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO

    def delete_user_by_username(self, username):
        session = database.get_session()
        query = session.query(
            model_user.UserModel).filter_by(username=username)
        try:
            user = query.first()
            session.delete(user)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO
