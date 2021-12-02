from dataclasses import dataclass

from board.req_objs import ValidReqObj

@dataclass
class PostListReqObj(ValidReqObj):
    page: int
    user_id: int

    # schema = {
    #
    # }
    #validate를 진행해야함
    @classmethod
    def from_dict(cls, adict = None, **kwargs):
        if adict is None:
            adict = kwargs

        return cls(
            page=adict['page'],
            user_id=adict['user_id']
        )

@dataclass
class PostCreateReqObj(ValidReqObj):
    user_id: int
    title: str
    content: str

    @classmethod
    def from_dict(cls, adict = None, **kwargs):
        if adict is None:
            adict = kwargs

        return cls(
            user_id=adict['user_id'],
            title=adict['title'],
            content=adict['content']
        )