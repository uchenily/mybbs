from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from mybbsbackend.database import Base
from datetime import datetime
from mybbsbackend.database.api import user as api_user
from mybbsbackend.database.api import category as api_category


class TopicModel(Base):

    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    author_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id"))
    agree = Column(Integer, default=0)
    disagree = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):

        user = api_user.UserAPI()
        category = api_category.CategoryAPI()
        return dict(
            id=self.id,
            title=self.title,
            author=user.get_one_by_id(self.author_id),
            content=self.content,
            category=category.get_one_by_id(self.category_id),
            agree=self.agree,
            disagree=self.disagree,
            created_time=self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            updated_time=self.updated_time.strftime("%Y-%m-%d %H:%M:%S")
        )
