from base_runner import BaseRunner
from util import get_publish_topic, get_group_id
import greengrasssdk
import os

class MqttRunner(BaseRunner):
    def __init__(self, group_id, topic):
        super().__init__(self, group_id)
        self.group_id = get_group_id()
        self.topic = get_publish_topic()
