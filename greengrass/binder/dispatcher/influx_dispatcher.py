import json
from collections import deque
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from .base_dispatcher import BaseDispatcher


TOKEN = 'Pm8wq9ftXpdI-F8ikJDtA3zlbdc1MnRVWkQRGM1-Zq7eBJ0rXFBJCE_haxIlheg3ja2uVSgUTOG_Q3aoOzfvgA=='
BUCKET = 'car-raw-data'
ORG = 'kpu'
URL = '3.34.87.77:8086'


"""
relay 되는 데이터의 형태

{'fields':
    [
        'engine_load',
        'engine_coolant_temp',
        'engine_rpm',
        'vehicle_speed',
        'maf_sensor',
        'o2_voltage',
        'throttle',
        'short_fuel_trim_bank',
        'long_fuel_trim_bank',
        'intake_air_temperature',
        'engine_runtime',
        'traveled_distance',
        'fuel_tank_level',
        'ambient_air_temperature',
        'engine_oil_temperature',
        'transmission_actual_gear'
    ],
    'values': [40, 64, 13, 40, 99, 99, 36, 94, 6, 6, 84, 47, 86, 20, 61, 2],
    'timestamp': 1618150407.851798
}
"""


class InfluxDispatcher(BaseDispatcher):
    def __init__(self):
        super().__init__()
        self.client = InfluxDBClient(url=URL, token=TOKEN)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def make_points(self, data: str) -> deque([Point]):
        dict_data = json.loads(data)
        point_queue = deque([])
        fields = dict_data.get('fields')
        values = dict_data.get('values')
        for i, v in enumerate(fields):
            point_queue.append(
                Point(v)\
                .tag('user', 'kim')\
                .field(v, values[i])\
                .time(datetime.utcnow(), WritePrecision.NS)
            )
        return point_queue

    def relay(self, data: str) -> None:
        points = self.make_points(data)
        for point in points:
            self.write_api.write(BUCKET, ORG, point)

    # TODO : We specify below things. Caution : We should not make dependencies.
    # 1. Influxdb url
    # 2. Influxdb table name
    # 3. Influxdb organzation, token, etc...

