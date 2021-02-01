from abc import ABC, abstractmethod

class BaseDispatcher(ABC):
    def __init__(self, device_id):
        self.device_id = device_id
    
    @abstractmethod
    def relay(self, data):
        pass #Dispatch 할 동작을 정의한다.