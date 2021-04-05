import json
from .base_dispatcher import BaseDispatcher


class TestDispatcher(BaseDispatcher):
    def __init__(self):
        pass

    def relay(self, data: str):
        print('dispatcher1 relayed data {}'.format(json.loads(data)))


class TestDispatcher2(BaseDispatcher):
    def __init__(self):
        pass

    def relay(self, data: str):
        print('dispatcher2 relayed data {}'.format(json.loads(data)))

class TestDispatcher3(BaseDispatcher):
    def __init__(self):
        pass

    def relay(self, data: str):
        print('dispatcher3 relayed data {}'.format(json.loads(data)))