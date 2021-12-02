from dataclasses import dataclass

from board.req_objs import ValidReqObj

@dataclass
class PostListReqObj(ValidReqObj):
    page: int
    user_id: int

    # schema = {
    #
    # }

@dataclass
class PostCreateReqObj(ValidReqObj):
    user_id: int
    title: str
    content: str