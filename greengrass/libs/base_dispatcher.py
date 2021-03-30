from abc import ABCMeta, abstractmethod

class BaseDispatcher(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def relay(self, data):
        pass


