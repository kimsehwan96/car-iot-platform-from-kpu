from device_codes.base_dispatcher import BaseDispatcher
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, WriteApi
from collections import deque
from datetime import datetime

TOKEN = ""
ORG = ""
BUCKET = ""
URL = ""
DATA_SOURCE = {
    "dataTypes" :[
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}
#TODO: How  to get above resource without hard-coding ?

class InfluxDispatcher(BaseDispatcher):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.data_source = DATA_SOURCE
        self.data_types = self.data_source.get('dataTypes')
        self.client = InfluxDBClient(url=URL, token=TOKEN)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def make_points(self, data:list) -> list(Point):
        point_list = deque([])
        for i, v in enumerate(data):
            point_list.append(
                Point(self.data_types[i])\
                    .tag("user", self.device_id)\
                    .filed("value", v)\
                    .time(datetime.utcnow(), WritePrecision.NS)
            )
        return point_list
    
    def relay(self, data):
        pass

    def write_data(self, points) -> None:
        for point in points:
            self.write_api.write(point)
        #TODO: check logic?
    
    



