from .mqtt_dispatcher import MqttDispatcher
from .websocket_dispatcher import WebSocketDispatcher
from .test_dispatcher import TestDispatcher
from .base_dispatcher import BaseDispatcher
from typing import List

class NotSupportedDispatcher(Exception):
    def __init__(self):
        super().__init__('지원하지 않는 Dispatcher 타입임')

CLASS_MAP = {
    'mqtt' : MqttDispatcher,
    'websocket' : WebSocketDispatcher,
    'test' : TestDispatcher
}

"""
config = ['test', 'websocket', 'test']
"""

def create_dispatchers(dispatcher_config: List[str]) -> List[BaseDispatcher]:
    dispatchers = []
    for v in dispatcher_config:
        dispatcher = CLASS_MAP.get(v)
        if dispatcher:
            dispatchers.append(dispatcher)
        else:
            raise NotSupportedDispatcher
    return dispatchers