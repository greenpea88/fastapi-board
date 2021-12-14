#use case에 전달할 때 사용할 req obj에 대한 기본 설정
#data에 대한 검증이 필요함
from dataclasses import asdict

from board.utils import FromDict


class ValidReqObj(FromDict):
    #유효한 request obj
    # schema = NotImplemented
    # validation 추가 필요

    # @classmethod
    def to_dict(self):
        #entity로부터 dictionary?
        # new_dict = {}
        new_dict = asdict(self)
        # for key in self.__annotations__.keys():
        #     value = getattr(self, key, None)
        #     print(f'key {key} value {value}')
        #     new_dict[key] = value
        return new_dict


    def __bool__(self):
        True

class InValidReqObj:
    #유효하지 않은 request obj
    def __bool__(self):
        False