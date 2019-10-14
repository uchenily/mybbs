from pecan import rest
from pecan import expose

from mybbsbackend.database.api import category as api_category
from mybbsbackend.database.model import category as model_category


class CategoryController(rest.RestController):
    def __init__(self):
        self.category = api_category.CategoryAPI()

    @expose('json')
    def get_one(self, id):
        return self.category.get_one_by_id(id)

    @expose('json')
    def get_all(self):
        return self.category.get_all()

    @expose('json')
    def post(self, category):
        category = model_category.CategoryModel(**category)
        return self.category.add_one(category)

    @expose('json')
    def put(self, category):
        return self.category.update_category(category)

    @expose('json')
    def delete(self, id):
        self.category.delete_category_by_id(id)
        return None
