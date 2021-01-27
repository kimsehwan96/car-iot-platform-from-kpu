import os
import csv
import traceback
import sys
import shutil
import requests
import boto3 #python aws sdk
from collections import deque
from _thread import start_new_thread, allocate_lock
from datetime import datetime, timedelta, timezone
from .base_dispatcher import BaseDispatcher
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, WriteApi

TOKEN = os.environ.get('INFLUX_TOKEN', None)
ORG = os.environ.get('INFLUX_ORG', None)
BUCKET = os.environ.get('INFLUX_BUCKET', None)
URL = os.environ.get('INFLUX_URL', None)

class InfluxDispatcher(BaseDispatcher):
    def __init__(self, edge_id):
        super().__init__(edge_id)
        self.queue = deque([])
        self.token = TOKEN
        self.org = ORG
        self.bucket = BUCKET
        self.URL = URL
        self.i_client = InfluxDBClient(self.url, self.token)
        self.write_client = self.i_client.write_api(write_options=SYNCHRONOUS)

    def relay(self, data):
        pass

    def parsing_data(self, data):
        pass
    #TODO: parsing raw data into INFLUXDB line protocol.