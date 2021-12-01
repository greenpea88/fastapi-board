#use case에 전달할 때 사용할 req obj에 대한 기본 설정
#data에 대한 검증이 필요함

class ValidReqObj:
    #유효한 request obj
    # schema = NotImplemented

    @classmethod
    #req obj를 만드는 factory 함수
    def from_dict(cls, adict):
        #dictionary로부터 entity?
        return cls

    def to_dict(self):
        #entity로부터 dictionary?
        new_dict = {}
        for key in self.__annotations__.keys():
            value = getattr(self, key, None)
            new_dict[key] = value

        return new_dict


    def __bool__(self):
        True

class InValidReqObj:
    #유효하지 않은 request obj
    def __bool__(self):
        False