from pecan import rest
from pecan import expose

from mybbsbackend.database.api import reply as api_reply
from mybbsbackend.database.model import reply as model_reply


class ReplyController(rest.RestController):
    def __init__(self):
        self.reply = api_reply.ReplyAPI()

    @expose('json')
    def get_one(self, name):
        return self.reply.get_one_by_name(name)

    @expose('json')
    def get_all(self):
        return self.reply.get_all()

    @expose('json')
    def post(self, reply):
        reply = model_reply.ReplyModel(**reply)
        return self.reply.add_one(reply)

    @expose('json')
    def put(self, reply):
        return self.reply.update_reply(reply)

    @expose('json')
    def delete(self, reply):
        self.reply.delete_reply_by_id(reply)
        return None
