#DB와 연결을 위해 필요한 것들을 모아둠
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from board.repositories.base import Base

db_user = 'greenpea'
db_password = ''
db_host = 'localhost'
db_port = '5432'
db_database = 'board'

dsn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
engine = create_engine(dsn, echo = True)
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine) #db 사용을 위한 session 연결


class MakeSession:
    session = None
    #session 사용을 위한 open/close를 python context를 이용하여 설정

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

class BaseRepo():
    model: Base = NotImplemented

    def __init__(self):
        db_user = 'greenpea'
        db_password = ''
        db_host = 'localhost'
        db_port = '5432'
        db_database = 'board'

        dsn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
        self.engine = create_engine(dsn, echo=True)
        Base.metadata.create_all(self.engine)

    @property
    def makeSession(self):

        @contextmanager
        def session():
            Session = sessionmaker(bind=self.engine)
            local_session = Session()
            try:
                yield local_session
            except:
                local_session.rollback()
                raise
            finally:
                local_session.close()

        return session

    def get(self, query, user_id):
        with self.makeSession as session:
            query - session.query(self.model)
