import traceback
import json

from .mqtt_dispatcher import MqttDispatcher
from .storage_dispatcher import StorageDispatcher

DISPATCHER_CLASS_MAP = {
    'MqttDispatcher' : MqttDispatcher,
    'StorageDispatcher' : StorageDispatcher
}

def create_dispatcher(edge_id, type:str):
    dispatcher_class = DISPATCHER_CLASS_MAP.get(type)

    if not dispatcher_class:
        return None
    
    return dispatcher_class(edge_id, )
