from fastapi import APIRouter

from board.repositories import MakeSession
from board.repositories.models import DBPost

from board.rest.routers.common import get_response

from board.usecases.board import PostListUseCase, PostCreateUseCase, PostModifyUseCase

from board.req_objs.board import PostListReqObj, PostCreateReqObj, PostModifyReqObj

from datetime import datetime
from typing import Optional

from board.rest.models.board import Post, ModifyPostInfo
from board.rest.routers.common import make_post_list

router = APIRouter()

# Base.metadata.create_all(engine)


@router.get("/")
def l7ConnectionCheck():
    return "success"


@router.get("/all_posts")
def getAllPost(page: Optional[int] = None):

    return get_response(PostListUseCase(), PostListReqObj.from_dict(page=page))

@router.get("/id_posts")
def getPostById(user_id: int):

    return get_response(PostListUseCase(), PostListReqObj.from_dict(user_id=user_id))

@router.post("/upload_post")
def uploadPost(post: Post):
    # Base.metadata.create_all(engine)
    request_params = {
        'user_id': post.user_id,
        'title': post.title,
        'content': post.content
    }
    get_response(PostCreateUseCase(), PostCreateReqObj.from_dict(**request_params))

@router.put('/modify_post')
def modifyPost(post_id: int, info: ModifyPostInfo):
    request_params = {
        'post_id': post_id,
        'title': info.title,
        'content': info.content
    }

    get_response(PostModifyUseCase(), PostModifyReqObj.from_dict(**request_params))
    # with MakeSession() as session:
    #     post = session.query(DBPost).filter_by(id=post_id).first()
    #
    #     if info.title != None:
    #         post.title = info.title
    #     if info.content != None:
    #         post.content = info.content
    #
    #     post.updated_at = datetime.utcnow()
    #     session.add(post)
    #     session.commit()
