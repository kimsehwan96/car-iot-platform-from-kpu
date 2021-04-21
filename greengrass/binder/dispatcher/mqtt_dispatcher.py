import greengrasssdk
from libs.util import get_cloud_topic

from .base_dispatcher import BaseDispatcher

mqtt = greengrasssdk.client('iot-data')


class MqttDispatcher(BaseDispatcher):
    def __init__(self):
        self._topic = get_cloud_topic()

    def publish(self, data):
        payload = data
        mqtt.publish(topic=self._topic, payload=payload)

    def relay(self, data: str):
        self.publish(data)
