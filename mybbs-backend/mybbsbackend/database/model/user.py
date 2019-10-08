from sqlalchemy import Column, Integer, String
from mybbsbackend.database import Base


class UserModel(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))

    def __json__(self):
        return dict(
            id=self.id,
            username=self.username,
            password=self.password
        )
