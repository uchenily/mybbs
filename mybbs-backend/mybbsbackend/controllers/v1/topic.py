from pecan import rest
from pecan import expose
from pecan import request

from mybbsbackend.database.api import topic as api_topic
from mybbsbackend.database.model import topic as model_topic


class TopicController(rest.RestController):
    def __init__(self):
        self.topic = api_topic.TopicAPI()

    @expose('json')
    def get_one(self, id):
        return self.topic.get_one_by_id(id)

    @expose('json')
    def get_all(self):
        flag = request.GET.get('flag')
        category_id = request.GET.get('category_id')
        if flag:
            return self.topic.get_list_by_flag(flag)
        elif category_id:
            return self.topic.get_list_by_category_id(category_id)
        else:
            return self.topic.get_all()

    @expose('json')
    def post(self, topic):
        topic = model_topic.TopicModel(**topic)
        return self.topic.add_one(topic)

    @expose('json')
    def put(self, topic):
        return self.topic.update_topic(topic)

    @expose('json')
    def delete(self, id):
        self.topic.delete_topic_by_id(id)
        return None
