from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from mybbsbackend.database import Base
from datetime import datetime
from mybbsbackend.database.api import user as api_user


class ReplyModel(Base):

    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):
        user = api_user.UserAPI()
        return dict(
            id=self.id,
            user=user.get_one_by_id(self.user_id),
            content=self.content,
            created_time=self.created_time,
            updated_time=self.updated_time
        )
