import threading
from time import sleep
from random import randint
from collections import deque
from typing import List

TEMPLATE = {
    "fields": [
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
    "values": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ]
}


class DummyPlugin:
    def __init__(self, period, template: dict):
        self.period = period
        self.template = template
        self._raw_data = None

    @property
    def raw_data(self):
        return self._raw_data

    @raw_data.setter
    def raw_data(self, data: deque):
        if type(data) is not deque:
            raise AssertionError("Data Type miss matched")
        self._raw_data = data

    def _random_data(self) -> deque:
        fields_length = len(self.template.get('fields'))
        return deque([randint(0, 100) for x in range(fields_length)])

    def _scheduler(self) -> None:
        while True:
            sleep(self.period)
            self.raw_data = self._random_data()
            # print(self.raw_data)

    def run(self):
        th = threading.Thread(target=self._scheduler)
        th.start()


def sub_thread(plugin_instance: DummyPlugin):
    while True:
        sleep(1)
        data = plugin_instance.raw_data
        print(data)



if __name__=='__main__':
    dp = DummyPlugin(1, TEMPLATE)
    dp.run()
    th2 = threading.Thread(target=sub_thread, args=(dp, ))
    th2.start()
    th2.join()