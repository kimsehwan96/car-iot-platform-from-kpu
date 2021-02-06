from abc import ABC, abstractmethod
from util import Profile


class BaseDispatcher(ABC):
    def __init__(self, device_id):
        self.device_id = device_id
        self.profile = Profile()
        self.data_fields = self.profile.get_data_types()

    @abstractmethod
    def relay(self, data):
        pass  # Dispatch 할 동작을 정의한다.

    # relay될 데이터의 포멧은 배열로, 우리가 받고싶은 DataTypes 순으로 정렬되어서 들어온다.
    # [1, 2, 3, 4] <- relaying data
    # ['rpm', 'speed', 'airTemp', 'oilTemp'] <- 예시 DataTypes
    # 따라서 relay된 데이터를 처리하는 코드는 기본으로 어떤 DataFields를 소모하는지 알고 있어야 함
