from fastapi import APIRouter, Depends
from typing import Optional

from board.repositories import BaseRepo
from board.rest.repo import get_post_repository
from board.rest.routers.common import get_response
from board.rest.models.board import Post, ModifyPostInfo

from board.usecases.board import PostListUseCase, PostCreateUseCase, PostModifyUseCase

from board.req_objs.board import PostListReqObj, PostCreateReqObj, PostModifyReqObj

router = APIRouter()

# Base.metadata.create_all(engine)


@router.get("/")
def l7ConnectionCheck():
    return "success"


@router.get("/all_posts")
def getAllPost(
        page: Optional[int] = None,
        repo: BaseRepo = Depends(get_post_repository)
    ):
    #특정 format(entity)를 통해 받은 정보들은 unwrapping하여서 전달해줌
    return get_response(PostListUseCase(repo=repo),
                        PostListReqObj.from_dict(page=page))

@router.get("/id_posts")
def getPostById(
        user_id: int,
        repo: BaseRepo = Depends(get_post_repository)
    ):

    return get_response(PostListUseCase(repo=repo),
                        PostListReqObj.from_dict(user_id=user_id))

@router.post("/upload_post")
def uploadPost(
        post: Post,
        repo: BaseRepo = Depends(get_post_repository)
    ):
    # Base.metadata.create_all(engine)
    request_params = {
        'user_id': post.user_id,
        'title': post.title,
        'content': post.content
    }
    get_response(PostCreateUseCase(repo=repo),
                 PostCreateReqObj.from_dict(**request_params))

@router.put('/modify_post')
def modifyPost(
        post_id: int, info: ModifyPostInfo,
        repo: BaseRepo = Depends(get_post_repository)
    ):
    request_params = {
        'post_id': post_id,
        'title': info.title,
        'content': info.content
    }

    get_response(PostModifyUseCase(repo=repo),
                 PostModifyReqObj.from_dict(**request_params))
