from dataclasses import dataclass

from board.req_objs import ValidReqObj

@dataclass
class PostListReqObj(ValidReqObj):
    page: int = None
    user_id: int = None

    # schema = {
    #
    # }

@dataclass
class PostCreateReqObj(ValidReqObj):
    user_id: int
    title: str
    content: str

@dataclass
class PostModifyReqObj(ValidReqObj):
    post_id: int
    title: str
    content: str
