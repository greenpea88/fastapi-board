from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from board.domain.board import PostInfo
from board.repositories.base import Base

from datetime import datetime

from board.utils import ToEntity


class DBUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    inactivate = Column(Boolean, default=False)

    def __repr__(self):
        return "<User(name='%s', email='%s', password='%s')>" % (
            self.name, self.email, self.password)

class DBPost(Base, ToEntity):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    user_id = Column(Integer, ForeignKey('users.id')) #post 작성한 user의 id를 foreign key로 설정
    user = relationship('DBUser') #실제 DB 칼럼으로 존재하는 변수 아님 -> 코드 상에서 쉽게 접근하기 위해 설정

    entity = PostInfo

    def to_entity(self):
        return self.entity.from_dict(
            {
                "user_name": self.user.name,
                "title": self.title,
                "content": self.content,
                "updated_at": self.updated_at.strftime("%m/%d/%Y, %H:%M:%S")
            }
        )