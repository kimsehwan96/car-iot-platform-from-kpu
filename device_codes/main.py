import socket
from collections import deque
from time import sleep
from can_plugin import CanPlugin

DATA_SOURCE = {
    "dataTypes" :[
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE",
        "SHORT_FUEL_TRIM_BANK",
        "LONG_FUEL_TRIM_BANK",
        "INTAKE_AIR_TEMPERATURE",
        "ENGINE_RUNTIME",
        "TRAVELED_DISTANCE",
        "FUEL_TANK_LEVEL",
        "AMBIENT_AIR_TEMPERATURE",
        "ENGINE_OIL_TEMPERATURE",
        "TRANSMISSION_ACTUAL_GEAR"
    ]
}

can_plugin = CanPlugin(DATA_SOURCE)
#can_plugin.send_request 의 리턴이 요청한 정보에 대한 값.

while True:
    sleep(1)
    res = can_plugin.send_request()
    # res = deque([1, 2, 3, 4])
    res_msg = ['{} : {} '.format(*x) for x in list(zip(DATA_SOURCE.get('dataTypes'), res))]
    print(res_msg)