from board.usecases import BaseUseCase

from board.req_objs import ValidReqObj

def res_to_model(res_mode, res):
    #use case가 로직을 처리하여 넘겨 받은 정보(entity)를 res model로 변경하여 넘겨줌
    pass

def get_response(usecase: BaseUseCase, req_obj: ValidReqObj):
    #router로부터 받은 req model을 받아서 usecase가 실행하도록 넘겨줌
    print(req_obj)
    res = usecase.execute(req_obj=req_obj) #entity의 형태로 받음
    return res
    # return res_to_model()