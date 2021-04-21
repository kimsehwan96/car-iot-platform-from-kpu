from _thread import start_new_thread
from abc import ABCMeta, abstractmethod


class BaseDispatcher(metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume 할 소비자 클래스의 베이스 클래스
    """

    def __init__(self):
        pass

    def run(self, data: str):
        start_new_thread(self.relay, (data, ))

    @abstractmethod
    def relay(self, data):
        """
        각 클래스 구현부에서 달라지는 메서드임.
        """
        raise NotImplementedError("추상 메서드입니다.")
