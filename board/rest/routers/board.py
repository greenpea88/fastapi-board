from fastapi import APIRouter
from pydantic import BaseModel

from sqlalchemy.orm import sessionmaker
from board.repositories import Base, engine
from board.repositories.models import DBUser, DBPost

from datetime import datetime

router = APIRouter()

Session = sessionmaker(bind=engine) #db 사용을 위한 session 연결

class MakeSession:
    session = None
    #session 사용을 위한 open/close를 python context를 이용하여 설정

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

class User(BaseModel):
    name: str
    email: str
    password: str

class Post(BaseModel):
    title: str
    content: str

@router.get("/")
def test():
    return "test"

@router.post("/join_user")
def joinUser(user: User):
    # Base.metadata.create_all(engine) 처음 1회만 생성하면 됨

    with MakeSession() as session:
        new_user = DBUser()
        new_user.name = user.name
        new_user.email = user.email
        new_user.password = user.password

        session.add(new_user)
        session.commit()

        result = session.query(DBUser).all()
    return result

@router.post("/upload_post")
def uploadPost(post: Post):
    # Base.metadata.create_all(engine)

    #post한 내용 등록
    with MakeSession() as session:
        new_post = DBPost()
        new_post.title = post.title
        new_post.content = post.content
        new_post.updated_at = datetime.utcnow()

        session.add(new_post)
        session.commit()

        result = session.query(DBPost).all()

    return result