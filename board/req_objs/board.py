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

        print(f'adict : {adict}')
        return cls(
            page=adict['page'],
            user_id=adict['user_id']
        )