from pecan import rest
from pecan import expose

from mybbsbackend.database.api import user as api_user
from mybbsbackend.database.model import user as model_user


class UserController(rest.RestController):
    def __init__(self):
        self.user = api_user.UserAPI()

    @expose('json')
    def get_one(self, username):
        return self.user.get_one_by_username(username)

    @expose('json')
    def get_all(self):
        return self.user.get_all()

    @expose('json')
    def post(self, user):
        user = model_user.UserModel(**user)
        return self.user.add_one(user)

    @expose('json')
    def delete(self, username):
        self.user.delete_user_by_username(username)
        return None
