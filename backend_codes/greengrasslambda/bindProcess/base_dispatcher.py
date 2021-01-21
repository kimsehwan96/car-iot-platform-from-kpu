from abc import ABC, abstractmethod

class BaseDispatcher(ABC):
    def __init__(self, edge_id, target):
        self.edge_id = edge_id
        self.target = target
    
    @abstractmethod
    def relay(self, data):
        pass #Dispatch 할 동작을 정의한다.