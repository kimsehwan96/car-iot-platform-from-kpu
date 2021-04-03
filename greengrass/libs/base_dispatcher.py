from abc import ABCMeta, abstractmethod


class BaseDispatcher(metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume할 소비자 클래스의 베이스 클래스
    """

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        """
        구현 클래스에서 구현해야 하며, 구현 내용은
        디스패쳐 스레드를 시작하도록 구현해야 함
        """
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def relay(self, data):
        """
        추상메서드로 구현 할 필요 없음. 수정 예정
        공통적으로 사용하는 인터페이스가 될 예정
        """
        pass
