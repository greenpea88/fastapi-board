from typing import List

from board.repositories.models import DBPost, DBUser
from board.repositories import MakeSession

from board.rest.models.board import ResPost

from board.usecases import BaseUseCase

from board.req_objs import ValidReqObj

def res_to_model(res_mode, res):
    #use case가 로직을 처리하여 생성한 정보를 req model로 변경하여 넘겨줌
    pass

def get_response(usecase: BaseUseCase, req_obj: ValidReqObj):
    #router로부터 받은 req model을 받아서 usecase가 실행하도록 넘겨줌
    print(req_obj)
    res = usecase.execute(req_obj=req_obj)
    return res
    # return res_to_model()

def make_post_list(posts: List[DBPost], session: MakeSession):
    res = []
    for post in posts:
        name = session.query(DBUser.name).filter_by(id=post.user_id).first()
        modify = False if post.created_at.strftime("%m/%d/%Y, %H:%M:%S") == post.updated_at.strftime(
            "%m/%d/%Y, %H:%M:%S") else True
        res.append(ResPost(user_name=name[0], title=post.title, content=post.content, modified=modify))
    return res