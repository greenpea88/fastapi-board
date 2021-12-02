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
        pass