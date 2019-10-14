from sqlalchemy.orm import exc

from mybbsbackend import database
from mybbsbackend.database.model import token as model_token


class TokenAPI:
    def get_one_by_username(self, username):
        session = database.get_session()
        query = session.query(
            model_token.TokenModel).filter_by(username=username)
        try:
            token = query.one()
            return token
        except exc.NoResultFound:
            return None

    def get_one_by_id(self, id):
        session = database.get_session()
        query = session.query(model_token.TokenModel).filter_by(id=id)
        try:
            token = query.one()
            return token
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_token.TokenModel)
        try:
            tokens = query.all()
            return tokens
        except exc.NoResultFound:
            return None

    def add_one_by_user_id(self, user_id):
        token = model_token.TokenModel(user_id=user_id)
        session = database.get_session()
        try:
            session.add(token)
            session.flush()
            session.commit()
            return token
        except Exception:
            pass
            # TODO

    def update_token(self, token):
        session = database.get_session()
        token_id = token.get('id')
        query = session.query(model_token.TokenModel).filter_by(id=token_id)
        try:
            # 'token' is a dict object here, not a model instance.
            # update() return a number, not a model instance.
            # in add_one(), 'token' stands a model instance.
            query.update(token)
            session.flush()
            session.commit()
            return token
        except exc.NoResultFound:
            pass
            # TODO

    def delete_token_by_user_id(self, user_id):
        session = database.get_session()
        query = session.query(
            model_token.TokenModel).filter_by(user_id=user_id)
        try:
            token = query.first()
            session.delete(token)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO
