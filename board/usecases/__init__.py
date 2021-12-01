#logic을 처리하는 usecase들을 모아놓음
#req obj를 받아서 logic을 처리함

class BaseUseCase():
    # # def __init__(self, repo):
    #     self.repo = repo

    def execute(self, req_obj):
        #validation 진행
        return self.process_request(req_obj)

    def process_request(self, req_obj):
        #logic 진행
        pass