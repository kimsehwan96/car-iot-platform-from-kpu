from abc import ABCMeta, abstractmethod
from _thread import start_new_thread


class BaseDispatcher(metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume할 소비자 클래스의 베이스 클래스
    """

    def __init__(self):
        pass

    def run(self, data: str):
        start_new_thread(self.relay, (data, ))

    @abstractmethod
    def relay(self, data):
        """
        추상메서드로 구현 할 필요 없음. 수정 예정
        공통적으로 사용하는 인터페이스가 될 예정
        받은 data는 json.loads로 객체화 하기
        """
        pass
