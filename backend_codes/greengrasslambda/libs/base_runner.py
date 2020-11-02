from abc import ABC, abstractmethod

class BaseRunner(ABC):
    def __init__(self, group_id):
        self.group_id = group_id

    @abstractmethod
    def relay(self, data):
        raise NotImplementedError

