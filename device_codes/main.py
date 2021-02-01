import socket
from time import sleep
from .can_plugin import CanPlugin

DATA_SOURCE = {
    "dataTypes" :[
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}

can_plugin = CanPlugin(DATA_SOURCE)
#can_plugin.send_request 의 리턴이 요청한 정보에 대한 값.

while True:
    sleep(1)
    print(can_plugin.send_request())

