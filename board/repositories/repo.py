from board.repositories import BaseRepo
from board.repositories.models import DBPost


class PostRepository(BaseRepo):
    model = DBPost

    def get(self, post_id = None, user_id = None, page = None):
        with self.makeSession as session:
            query = session.query(self.model)
            if user_id:
                posts = query.filter(self.model.id==user_id)
            if page:
                self.get_all(query, page=page)
