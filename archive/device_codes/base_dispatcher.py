from abc import ABC, abstractmethod
from libs.util import Profile


class BaseDispatcher(ABC):
    def __init__(self, data_list) -> None:
        pass

    @abstractmethod
    def relay(self, data) -> None:
        pass