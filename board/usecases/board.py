from datetime import datetime

from board.usecases import BaseUseCase

from board.repositories import MakeSession
from board.repositories.models import DBPost
from board.rest.routers.common import make_post_list

class PostListUseCase(BaseUseCase):
    def process_request(self, req_obj):
        # posts = self.repo
        # 일단은 DBPost로 넣었는데 이 값을 이제 req_obj로 변경해야함
        #   >> 세션 관련 작업은 repo로 빼줘야할 필요가 있음
        req_obj = req_obj.to_dict()

        with MakeSession() as session:
            query = session.query(DBPost)
            # 1. user_id 값이 있는 경우
            if req_obj['user_id'] is not None:
                posts = query.filter_by(user_id=req_obj['user_id']).all()
                if not posts:
                    return 'post가 존재하지 않습니다.'
            else:
                if not req_obj['page']:
                    posts = query.all()
                    if not posts:
                        return 'post is not exist'
                # 2. pagination이 필요한 경우
                else:
                    offset = (req_obj['page'] - 1) * 5
                    posts = query.offset(offset).limit(5).all()
        res = make_post_list(posts, session)
        return res

class PostCreateUseCase(BaseUseCase):
    def process_request(self, req_obj):
        #이 값을 repo에 넘겨줘야하는 값임(?)
        req_obj = req_obj.to_dict()
        # post한 내용 등록
        with MakeSession() as session:
            new_post = DBPost()
            new_post.user_id = req_obj['user_id']
            new_post.title = req_obj['title']
            new_post.content = req_obj['content']

            session.add(new_post)
            session.commit()

class PostModifyUseCase(BaseUseCase):
    def process_request(self, req_obj):
        req_obj = req_obj.to_dict()

        with MakeSession() as session:
            post = session.query(DBPost).filter_by(id=req_obj['post_id']).first()

            # if req_obj['info']['title'] != None:
            #     post.title = req_obj['info']['title']
            # if req_obj['info']['content'] != None:
            #     post.content = req_obj['info']['content']

            if req_obj['title'] != None:
                post.title = req_obj['title']
            if req_obj['content'] != None:
                post.content = req_obj['content']

            post.update_at = datetime.utcnow()
            session.add(post)
            session.commit()