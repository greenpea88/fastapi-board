from fastapi import APIRouter

from board.repositories import MakeSession
from board.repositories.models import DBPost

from board.rest.routers.common import get_response

from board.usecases.board import PostListUseCase

from board.req_objs.board import PostListReqObj

from datetime import datetime
from typing import Optional

from board.rest.models.board import Post, ModifyPostInfo
from board.rest.routers.common import make_post_list

router = APIRouter()

# Base.metadata.create_all(engine)


@router.get("/")
def l7ConnectionCheck():
    return "success"


@router.get("/all_post")
def getAllPost(page: Optional[int] = None):
    request_params = {
        'page': page,
        'user_id': None
    }
    test_res = get_response(PostListUseCase(), PostListReqObj.from_dict(**request_params))
    print(f'test_res : {test_res}')
    with MakeSession() as session:
        posts = session.query(DBPost)
        if not page:
            posts = posts.all()
            if posts is None:
                return 'post가 존재하지 않습니다.'

        else:
            offset = (page - 1) * 5
            posts = posts.offset(offset).limit(5).all()
        res = make_post_list(posts, session)
    return res
    # return get_response(page)

@router.get("/id_posts/{user_id}")
def getPostById(user_id: int):
    # request_params = {
    #     'page': None,
    #     'user_id': user_id
    # }
    # get_response(PostListUseCase, PostListReqObj.from_dict(request_params))
    with MakeSession() as session:
        posts = session.query(DBPost).filter_by(user_id=user_id).all()
        if posts is None:
            return 'post가 존재하지 않습니다.'
        res = make_post_list(posts, session)

    return res

@router.post("/upload_post")
def uploadPost(post: Post):
    # Base.metadata.create_all(engine)

    #post한 내용 등록
    with MakeSession() as session:
        new_post = DBPost()
        new_post.user_id = post.user_id
        new_post.title = post.title
        new_post.content = post.content

        session.add(new_post)
        session.commit()

        result = session.query(DBPost).all()

    return result

@router.put('/modify_post')
def modifyPost(post_id: int, info: ModifyPostInfo):

    with MakeSession() as session:
        post = session.query(DBPost).filter_by(id=post_id).first()

        if info.title != None:
            post.title = info.title
        if info.content != None:
            post.content = info.content

        post.updated_at = datetime.utcnow()
        session.add(post)
        session.commit()
