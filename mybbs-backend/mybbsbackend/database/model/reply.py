from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from mybbsbackend.database import Base
from datetime import datetime
from mybbsbackend.database.api import user as api_user
from mybbsbackend.database.api import topic as api_topic


class ReplyModel(Base):

    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    content = Column(Text)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):
        user = api_user.UserAPI()
        topic = api_topic.TopicAPI()
        return dict(
            id=self.id,
            user=user.get_one_by_id(self.user_id),
            topic=topic.get_one_by_id(self.topic_id),
            content=self.content,
            created_time=self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            updated_time=self.updated_time.strftime("%Y-%m-%d %H:%M:%S")
        )
