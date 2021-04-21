from random import randint
from libs.plugin import run_plugin_thread
from libs.base_plugin import BasePlugin

TEST_FIELDS = [
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
    ]

def handler(event, context):
    pass


class TestPlugin(BasePlugin):
    def __init__(self, fields):
        super().__init__(fields, option={})
    def collect_data(self):
        self.data = [randint(0, 100) for x in range(16)]
        print('this is bufferd data: ', self.data)


tp = TestPlugin(TEST_FIELDS)


def run():
    run_plugin_thread(tp.entry)


if __name__ == '__main__':
    pass
else:
    run()
