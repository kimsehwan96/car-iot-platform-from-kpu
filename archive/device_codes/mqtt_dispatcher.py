import os
import json
import greengrasssdk
from base_dispatcher import BaseDispatcher

MSG_MAX_SIZE = 1024 * 128  # greengrass mqtt's max msg size is 128kb
IS_LOCAL = os.environ.get('LOCAL_RUNTIME')

mqtt = greengrasssdk.client('iot-data') if not IS_LOCAL else None


# If we test this code in local machine then we should not make greengrasssdk client

class MqttDispatcher(BaseDispatcher):
    def __init__(self, device_id) -> None:
        super().__init__(device_id)
        self.topic = "test/data"  # TODO: replace this topic in production

    def publish(self, data):
        payload = json.dumps(data)
        if mqtt:
            mqtt.publish(topic=self.topic, payload=payload)
        else:
            print(json.dumps(payload, ident=2))

    def relay(self, data):
        if data:
            self.publish(data)
        else:
            raise Exception("No data..")
