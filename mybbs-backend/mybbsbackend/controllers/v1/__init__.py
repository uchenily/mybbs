from mybbsbackend.controllers.v1.user import UserController
from mybbsbackend.controllers.v1.topic import TopicController
from mybbsbackend.controllers.v1.category import CategoryController
from mybbsbackend.controllers.v1.reply import ReplyController


class Controller:

    users = UserController()
    topics = TopicController()
    categories = CategoryController()
    replies = ReplyController()
