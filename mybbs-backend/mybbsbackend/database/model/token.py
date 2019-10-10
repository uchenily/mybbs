import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from mybbsbackend.database import Base
from mybbsbackend.database.api import user as api_user


class TokenModel(Base):

    __tablename__ = 'tokens'
    id = Column(String(36),
                default=lambda: str(uuid.uuid4()),
                primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime,
                          default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):
        user = api_user.UserAPI()
        return dict(id=self.id,
                    username=user.get_one_by_id(self.user_id).username,
                    created_time=self.created_time,
                    updated_time=self.updated_time)
