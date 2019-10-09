from sqlalchemy.orm import exc

from mybbsbackend import database
from mybbsbackend.database.model import category as model_category


class CategoryAPI:
    def get_one_by_name(self, name):
        session = database.get_session()
        query = session.query(
            model_category.CategoryModel).filter_by(name=name)
        try:
            category = query.one()
            return category
        except exc.NoResultFound:
            return None

    def get_one_by_id(self, id):
        session = database.get_session()
        query = session.query(
            model_category.CategoryModel).filter_by(id=id)
        try:
            category = query.one()
            return category
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_category.CategoryModel)
        try:
            categories = query.all()
            return categories
        except exc.NoResultFound:
            return None

    def add_one(self, category):
        session = database.get_session()
        try:
            session.add(category)
            session.flush()
            session.commit()
            return category
        except Exception:
            pass
            # TODO

    def update_category(self, category):
        session = database.get_session()
        category_id = category.get('id')
        query = session.query(model_category.CategoryModel).filter_by(
            id=category_id)
        try:
            query.update(category)
            session.flush()
            session.commit()
            return category
        except exc.NoResultFound:
            pass
            # TODO

    def delete_category_by_id(self, category):
        session = database.get_session()
        category_id = category.get('id')
        query = session.query(
            model_category.CategoryModel).filter_by(id=category_id)
        try:
            category = query.one()
            session.delete(category)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            pass
            # TODO
