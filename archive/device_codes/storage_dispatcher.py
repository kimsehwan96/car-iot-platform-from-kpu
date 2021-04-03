import os
import csv
import traceback
import sys
from collections import deque
from _thread import start_new_thread, allocate_lock
from datetime import datetime, timedelta, timezone
from base_dispatcher import BaseDispatcher
from util import Profile

LOCAL_DATA_PATH = os.environ.get('LOCAL_DATA_PATH', '/kpu/raw_data')
S3_SAVE_BUCKET = os.environ.get('S3_SAVE_BUCKET', 'sehwan-test-bucket')

DATA_SOURCE = {
    "dataTypes": [
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}


class StorageDispatcher(BaseDispatcher):
    def __init__(self, data_list):
        super().__init__(data_list)

    def write_csv(self, filepath, data):
        pass

    def _merge(self):
        pass

    def _save(self):
        pass

    def relay(self, data):
        pass
