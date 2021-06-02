from random import randint
from libs.plugin import run_plugin_thread
from libs.base_plugin import BasePlugin

TEST_FIELDS = [
    'engine_load',
    'engine_rpm',
    'intake_manifold_absolute_pressure',
    'vehicle_speed',
    'throttle',
    'short_fuel_trim_bank',
    'engine_runtime',
    'traveled_distance',
    'fuel_tank_level',
    'ambient_air_temperature',
    'maf_sensor',
    'oxygen_sensor',
    'short_term_fuel_efficiency',
    'average_fuel_efficiency'
]


def handler(event, context):
    pass


class TestPlugin(BasePlugin):
    def __init__(self, fields):
        super().__init__(fields, option={})
        self._data_len = len(fields)

    def collect_data(self):
        self.data = [randint(0, 100) for x in range(self._data_len)]
        print('this is buffered data: ', self.data)


tp = TestPlugin(TEST_FIELDS)


def run():
    run_plugin_thread(tp.entry)


if __name__ == '__main__':
    pass
else:
    run()
