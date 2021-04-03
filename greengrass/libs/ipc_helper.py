import os
import json
import time
import threading
import greengrasssdk

from typing import List
from collections import deque
from datetime import datetime, timedelta
from .util import get_ipc_topic


class IpcHelper:
    """
    IPC는 mqtt를 이용해서 우선 진행 해볼 예정.
    가능하다면 unix domain socket?
    """

    def __init__(self, ipc_topic, option: {}):
        self.ipc_topic = ipc_topic
        self._channel = greengrasssdk.client('iot-data')
        self._buffer = []

    def get_topic(self):
        return self.ipc_topic

    def push_data(self, data: List):
        self._buffer = data

    def scheduler(self):
        buf_len = len(self._buffer)
        if buf_len == 0:
            print('no buf')
            return

        message = {
            'payload': {
                'fields': [
                    "engine_load",
                    "engine_coolant_temp",
                    "engine_rpm",
                    "vehicle_speed",
                    "maf_sensor",
                    "o2_voltage",
                    "throttle",
                    "short_fuel_trim_bank",
                    "long_fuel_trim_bank",
                    "intake_air_temperature",
                    "engine_runtime",
                    "traveled_distance",
                    "fuel_tank_level",
                    "ambient_air_temperature",
                    "engine_oil_temperature",
                    "transmission_actual_gear"
                ],
                'values': self._buffer
            }
        }

        self._channel.publish(
            topic=self.ipc_topic,
            payload=json.dumps(message)
        )

        print(f'message publish done by topic : ,{self.ipc_topic}, message : {message}')

    def scheduler_start(self):
        def wrapper():
            while True:
                self.scheduler()
                time.sleep(1)

        threading.Thread(target=wrapper).start()
