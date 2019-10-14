from sqlalchemy import Column, Integer, String, DateTime
from mybbsbackend.database import Base
from datetime import datetime


class UserModel(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):
        return dict(
            id=self.id,
            username=self.username,
            password="****",
            created_time=self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            updated_time=self.updated_time.strftime("%Y-%m-%d %H:%M:%S")
        )
