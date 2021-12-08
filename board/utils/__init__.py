from typing import List

# from board.repositories import MakeSession
# from board.repositories.models import DBPost, DBUser
# from board.rest.models.board import ResPost

class FromDict:
    @classmethod
    # req obj를 만드는 factory 함수
    def from_dict(cls, adict=None, **kwarg):
        # dict로부터 entity
        if adict is None:
            adict = kwarg
        print(f'adict : {adict}')
        return cls(**adict)

class ToEntity:
    entity = NotImplemented

    # @classmethod
    def to_entity(self):
        pass

# def make_post_list(posts: List[DBPost], session: MakeSession):
#     res = []
#     for post in posts:
#         name = session.query(DBUser.name).filter_by(id=post.user_id).first()
#         modify = False if post.created_at.strftime("%m/%d/%Y, %H:%M:%S") == post.updated_at.strftime(
#             "%m/%d/%Y, %H:%M:%S") else True
#         res.append(ResPost(user_name=name[0], title=post.title, content=post.content, modified=modify))
#     return res