from sqlalchemy.orm import exc
from mybbsbackend import database
from mybbsbackend.database.model import topic as model_topic


class TopicAPI:
    def get_one_by_id(self, id):
        session = database.get_session()
        query = session.query(
            model_topic.TopicModel).filter_by(id=id)
        try:
            topic = query.one()
            return topic
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_topic.TopicModel)
        try:
            topics = query.all()
            return topics
        except exc.NoResultFound:
            return None

    def get_list_by_flag(self, flag):
        session = database.get_session()
        model = model_topic.TopicModel
        if flag == 'agree':
            query = session.query(model).order_by(model.agree.desc()).limit(10)
        elif flag == 'latest':
            query = session.query(model).order_by(
                model.updated_time.desc()).limit(10)
        elif flag == 'all':
            query = session.query(model).limit(10)
        elif flag == 'hot':
            query = session.query(model).order_by(
                model.disagree.desc()).limit(10)
        else:
            query = session.query(model)
        try:
            topics = query.all()
            return topics
        except exc.NoResultFound:
            return None

    def get_list_by_category_id(self, category_id):
        session = database.get_session()
        query = session.query(model_topic.TopicModel).filter_by(
            category_id=category_id)
        try:
            topics = query.all()
            return topics
        except exc.NoResultFound:
            return None

    def add_one(self, topic):
        session = database.get_session()
        try:
            session.add(topic)
            session.flush()
            session.commit()
            return topic
        except Exception:
            pass
            # TODO

    def update_topic(self, topic):
        session = database.get_session()
        topic_id = topic.get('id')
        query = session.query(model_topic.TopicModel).filter_by(
            id=topic_id)
        try:
            query.update(topic)
            session.flush()
            session.commit()
            return topic
        except exc.NoResultFound:
            pass
            # TODO

    def delete_topic_by_id(self, id):
        session = database.get_session()
        query = session.query(
            model_topic.TopicModel).filter_by(id=id)
        try:
            topic = query.one()
            session.delete(topic)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO
