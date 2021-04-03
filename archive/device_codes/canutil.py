from enum import Enum
import can

DATA_TYPE_INDEX = 2


class NotSupportedDataTypeException(Exception):
    def __init__(self):
        super().__init__("지원하지 않는 데이터 타입입니다.")


class CanDataType(Enum):
    ENGINE_LOAD = 0x04
    ENGINE_COOLANT_TEMP = 0x05
    ENGINE_RPM = 0x0C
    VEHICLE_SPEED = 0x0D
    MAF_SENSOR = 0x10
    O2_VOLTAGE = 0x14
    THROTTLE = 0x11
    SHORT_FUEL_TRIM_BANK = 0x06
    LONG_FUEL_TRIM_BANK = 0x08
    INTAKE_AIR_TEMPERATURE = 0x0F
    ENGINE_RUNTIME = 0x1F
    TRAVELED_DISTANCE = 0x31
    FUEL_TANK_LEVEL = 0x2F
    AMBIENT_AIR_TEMPERATURE = 0x46
    ENGINE_OIL_TEMPERATURE = 0x5C
    TRANSMISSION_ACTUAL_GEAR = 0xA4

    PID_REQUEST = 0x7DF
    PID_REPLY = 0x7E8


class MetaSingleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        

class CanRequestMessage(metaclass=MetaSingleton):
    # TODO: change this class as singleton
    def __str__(self):
        return "{}".format(self.message)

    def __init__(self, data_type: CanDataType) -> None:
        self.data_type = data_type  # ENUM
        self.message = [0x02,
                        0x01,
                        self.data_type.value,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x00]

    def get_type(self) -> CanDataType.name:
        return self.data_type.name


class CanDataConvert:
    @staticmethod
    def convert(recv_msg: can.Message) -> int:
        data_type = recv_msg.data[DATA_TYPE_INDEX]
        try:
            handler = getattr(CalculateData, CanDataType(data_type).name.lower())
            return handler(recv_msg)
        except AttributeError:
            raise NotSupportedDataTypeException


class CalculateData:

    @staticmethod
    def engine_coolant_temp(recv_msg) -> int:
        return recv_msg[3] - 40

    @staticmethod
    def engine_load(recv_msg) -> int:
        return round((100 / 255) * recv_msg[3], 2)

    @staticmethod
    def engine_rpm(recv_msg) -> int:
        return round(((recv_msg * 256) + recv_msg[4]) / 4, 2)

    @staticmethod
    def vehicle_speed(recv_msg) -> int:
        return recv_msg[3]

    @staticmethod
    def throttle(recv_msg) -> int:
        return round((recv_msg[3] * 100) / 255, 2)

    @staticmethod
    def short_fuel_trim_bank(recv_msg) -> int:
        return round(((100 / 128) * recv_msg[3]) - 100, 2)

    @staticmethod
    def long_fuel_trim_bank(recv_msg) -> int:
        return round(((100 / 128) * recv_msg[3]) - 100, 2)

    @staticmethod
    def short_fuel_trim_bank(recv_msg) -> int:
        return round(((100 / 128) * recv_msg[3]) - 100, 2)

    @staticmethod
    def intake_air_temperature(recv_msg) -> int:
        return recv_msg[3] - 40

    @staticmethod
    def throttle_position(recv_msg) -> int:
        return round((100 / 256) * recv_msg[3], 2)

    @staticmethod
    def engine_runtime(recv_msg) -> int:
        return 256 * recv_msg[3] + recv_msg[4]

    @staticmethod
    def traveled_distance(recv_msg) -> int:
        return 256 * recv_msg[3] + recv_msg[4]

    @staticmethod
    def fuel_tank_level(recv_msg) -> int:
        return round((100 / 255) * recv_msg[3], 2)

    @staticmethod
    def ambient_air_temperature(recv_msg) -> int:
        return recv_msg[3] - 40

    @staticmethod
    def engine_oil_temperature(recv_msg) -> int:
        return recv_msg[3] - 40

    @staticmethod
    def transmission_actual_gear(recv_msg) -> int:
        return recv_msg[3]


if __name__ == '__main__':
    msg1 = CanRequestMessage(CanDataType.ENGINE_LOAD)
    msg2 = CanRequestMessage(CanDataType.ENGINE_COOLANT_TEMP)
    print(msg1, msg2)
