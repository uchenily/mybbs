from pecan import rest
from pecan import expose

from mybbsbackend.database.api import token as api_token
from mybbsbackend.database.api import user as api_user


class TokenController(rest.RestController):
    def __init__(self):
        self.token = api_token.TokenAPI()
        self.user = api_user.UserAPI()

    @expose('json')
    def get_one(self, username, password):
        return self.token.get_one_by_username_and_password(username, password)

    @expose('json')
    def get_all(self):
        return self.token.get_all()

    @expose('json')
    def post(self, data):
        username = data.get("username")
        password = data.get("password")
        user = self.user.get_one_by_username(username)
        if user and user.password == password:
            return self.token.add_one_by_user_id(user.id)
        else:
            return None

    @expose('json')
    def put(self, token):
        return self.token.update_token(token)

    @expose('json')
    def delete(self, token):
        self.token.delete_token_by_id(token)
        return None
