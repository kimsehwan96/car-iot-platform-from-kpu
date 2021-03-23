from base_dispatcher import BaseDispatcher
from typing import List
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, WriteApi
from collections import deque
from datetime import datetime

TOKEN = ""
ORG = ""
BUCKET = ""
URL = ""
DATA_SOURCE = {
    "dataTypes": [
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}


# TODO: How  to get above resource without hard-coding ?

class InfluxDispatcher(BaseDispatcher):
    def __init__(self, data_list) -> None:
        super().__init__(data_list)

    def make_points(self, data: list) -> List[Point]:
        point_list = deque([])
        for i, v in enumerate(data):
            point_list.append(
                Point(self.data_list[i]) \
                    .tag("user", "admin") \
                    .filed("value", v) \
                    .time(datetime.utcnow(), WritePrecision.NS)
            )
        return point_list

    def relay(self, data):
        pass

    def write_data(self, points) -> None:
        for point in points:
            self.write_api.write(point)
        # TODO: check logic?
