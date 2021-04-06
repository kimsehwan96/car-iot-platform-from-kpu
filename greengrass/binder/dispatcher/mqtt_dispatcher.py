from libs.util import get_cloud_topic
from .base_dispatcher import BaseDispatcher
import greengrasssdk

mqtt = greengrasssdk.client('iot-data')


class MqttDispatcher(BaseDispatcher):
    def __init__(self):
        self._topic = get_cloud_topic()

    def publish(self, data):
        payload = data
        mqtt.publish(topic=self._topic, payload=payload)
        print(f'published to cloud with topic {self._topic}')
        print(f'data : {data}')

    def relay(self, data: str):
        self.publish(data)
