from sqlalchemy.orm import exc

from mybbsbackend import database
from mybbsbackend.database.model import reply as model_reply


class ReplyAPI:
    def get_one_by_id(self, id):
        session = database.get_session()
        query = session.query(
            model_reply.ReplyModel).filter_by(id=id)
        try:
            reply = query.one()
            return reply
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_reply.ReplyModel)
        try:
            replys = query.all()
            return replys
        except exc.NoResultFound:
            return None

    def add_one(self, reply):
        session = database.get_session()
        try:
            session.add(reply)
            session.flush()
            session.commit()
            return reply
        except Exception:
            pass
            # TODO

    def update_reply(self, reply):
        session = database.get_session()
        reply_id = reply.get('id')
        query = session.query(model_reply.ReplyModel).filter_by(
            id=reply_id)
        try:
            query.update(reply)
            session.flush()
            session.commit()
            return reply
        except exc.NoResultFound:
            pass
            # TODO

    def delete_reply_by_id(self, reply):
        session = database.get_session()
        reply_id = reply.get('id')
        query = session.query(
            model_reply.ReplyModel).filter_by(id=reply_id)
        try:
            reply = query.one()
            session.delete(reply)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO
