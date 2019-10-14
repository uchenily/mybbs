from sqlalchemy import Column, Integer, String, DateTime, Text
from mybbsbackend.database import Base
from datetime import datetime
#from mybbsbackend.database.model.user import UserModel


class CategoryModel(Base):

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            created_time=self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            updated_time=self.updated_time.strftime("%Y-%m-%d %H:%M:%S")
        )
