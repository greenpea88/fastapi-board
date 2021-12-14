from board.repositories import BaseRepo
from board.repositories.repo import PostRepository


class RepositoryFactory:
    def __init__(self, repo=BaseRepo):
        self.repo = repo

    #클래스 인스턴스를 불렀을 때 실행되는 함수
    def __call__(self):
        repo = self.repo()

        return repo

get_post_repository = RepositoryFactory(PostRepository)