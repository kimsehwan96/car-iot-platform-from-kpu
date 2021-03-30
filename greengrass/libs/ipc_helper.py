import os
import json
import time
import threading
import greengrasssdk

from collections import deque
from datetime import datetime, timedelta
from .util import get_ipc_topic


class IpcHelper:
    def __init__(self, ipc_topic, option: {}):
        self.ipc_topic = ipc_topic
        self._channel = greengrasssdk.client('iot-data')

    def get_topic(self):
        return self.ipc_topic

    def push_data(self):
        pass

    def scheduler(self):
        pass

    def scheduler_start(self):
        pass
