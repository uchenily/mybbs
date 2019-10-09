from mybbsbackend.controllers.v1.user import UserController
from mybbsbackend.controllers.v1.topic import TopicController
from mybbsbackend.controllers.v1.category import CategoryController


class Controller:

    users = UserController()
    topics = TopicController()
    categories = CategoryController()
