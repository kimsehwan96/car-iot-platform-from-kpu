from abc import ABCMeta, abstractmethod
from _thread import start_new_thread
from meta_singleton import Singleton

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


class BaseDispatcher(Singleton, metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume할 소비자 클래스의 베이스 클래스
    """

    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        start_new_thread(self.relay, args, kwargs=kwargs)

    @abstractmethod
    def relay(self, data):
        """
        추상메서드로 구현 할 필요 없음. 수정 예정
        공통적으로 사용하는 인터페이스가 될 예정
        """
        pass

# TODO : 간헐적으로 이전값을 그대로 들고 다시보내는 경우가 있음. 해결해야 함
