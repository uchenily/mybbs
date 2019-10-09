from sqlalchemy.orm import exc

from mybbsbackend import database
from mybbsbackend.database.model import user as model_user


class UserAPI:
    def get_one_by_username(self, username):
        session = database.get_session()
        query = session.query(
            model_user.UserModel).filter_by(username=username)
        try:
            user = query.one()
            return user
        except exc.NoResultFound:
            return None

    def get_one_by_id(self, id):
        session = database.get_session()
        query = session.query(model_user.UserModel).filter_by(id=id)
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
            return user
        except Exception:
            pass
            # TODO

    def update_user(self, user):
        session = database.get_session()
        user_id = user.get('id')
        query = session.query(model_user.UserModel).filter_by(id=user_id)
        try:
            # 'user' is a dict object here, not a model instance.
            # update() return a number, not a model instance.
            # in add_one(), 'user' stands a model instance.
            query.update(user)
            session.flush()
            session.commit()
            return user
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
