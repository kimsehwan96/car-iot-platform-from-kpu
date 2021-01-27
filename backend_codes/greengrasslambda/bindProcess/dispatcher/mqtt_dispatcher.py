import os
import json
import greengrasssdk
from .base_dispatcher import BaseDispatcher
from libs.util import get_publish_topic

IS_LOCAL = os.environ.get('LOCAL_RUNTIME')

mqtt = greengrasssdk.client('iot-data') if not IS_LOCAL else None

class MqttDispatcher(BaseDispatcher):
    def __init__(self, edge_id):
        super().__init__(edge_id)
        self.topic = get_publish_topic
    
    def publish(self, data):
        if mqtt:
            mqtt.publish(topic=self.topic, payload=data)
        else:
            print(data)
        
    def relay(self, data):
        print('dispatcher type: {}'.format(self.edge_id))
        if data.get('values') is None:
            print('empty buffer is not sent to cloud....')
        else:
            self.publish(data)
        
        # 결정 할 것
        # data를 dict object로 관리할것인지, string obj로 관리할것인지.