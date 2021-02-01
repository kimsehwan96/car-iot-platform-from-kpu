import os
import csv
import traceback
import sys
from collections import deque
from _thread import start_new_thread, allocate_lock
from datetime import datetime, timedelta, timezone
from base_dispatcher import BaseDispatcher

DATA_SOURCE = {
    "dataTypes" :[
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}

class StorageDispatcher(BaseDispatcher):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.data_source = DATA_SOURCE
        self.queue = deque([])
        self.minute = None

    def write_csv(self, filepath, data):
        pass

    def _merge(self):
        pass

    def _save(self):
        pass

    def relay(self, data):
        pass
