from board.repositories import BaseRepo
from board.repositories.models import DBPost, DBUser


class PostRepository(BaseRepo):
    model = DBPost

    def get(self, post_id = None, user_id = None, page = None):
        with self.makeSession() as session:
            query = session.query(self.model).order_by(self.model.id)
            if user_id:
                query = self.get_all(query, user_id, page)
            if page:
                query = self.get_all(query, page=page)
            posts = query.all()

            if not posts:
                return None
            for post in posts:
                print(post.user)

        # for post in posts:
        #     print(post.to_entity())
        return [post.to_entity() for post in posts]
        # return posts

class UserRepository(BaseRepo):
    model = DBUser

    def get(self, post_id = None, user_id = None, page = None):
        with self.makeSession as session:
            query = session.query(self.model)
            if user_id:
                user = query.filter(self.model.id==user_id).first()

        #entity로 전환하여 전달해야함
