from enum import Enum

DATA_TYPE_INDEX = 2


class NotSupportedDataTypeException(Exception):
    def __init__(self):
        super().__init__("지원하지 않는 데이터 타입입니다.")


class CanDataType(Enum):
    """
    OBD2 PIDS : https://en.wikipedia.org/wiki/OBD-II_PIDs

    차량 제조사별 확장 PID 및 다른 PID가 존재할 수 있다. 확인 필요
    """
    ENGINE_LOAD = 0x04
    SHORT_FUEL_TRIM_BANK = 0x06
    LONG_FUEL_TRIM_BANK = 0x07
    INTAKE_MANIFOLD_ABSOLUTE_PRESSURE = 0x0b
    ENGINE_RPM = 0x0C
    VEHICLE_SPEED = 0x0d
    INTAKE_AIR_TEMPERATURE = 0x0F
    MAF_SENSOR = 0x10
    THROTTLE = 0x11
    ENGINE_RUNTIME = 0x1F
    TRAVELED_DISTANCE = 0x31  # since Error code cleared !
    FUEL_TANK_LEVEL = 0x2F
    OXYGEN_SENSOR = 0x34
    AMBIENT_AIR_TEMPERATURE = 0x46
    SHORT_TERM_FUEL_EFFICIENCY = 0x00  # this is dummy
    AVERAGE_FUEL_EFFICIENCY = 0x00  # this is dummy

    # Request & Response
    PID_REQUEST = 0x7DF
    PID_REPLY = 0x7E8

    # PID MODES
    SHOW_CURRENT_DATA = 0x01
    SHOW_FREEZE_FRAME_DATA = 0x02
    SHOW_TROUBLE_CODES = 0x03


class CanRequestMessage:
    # TODO: change this class as singleton
    def __str__(self) -> str:
        return "{}".format(self.message)

    def __init__(self, data_type) -> None:
        self.data_type = data_type  # ENUM
        self.message = [0x02,
                        CanDataType.SHOW_CURRENT_DATA.value,
                        self.data_type.value,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x00]

    def get_type(self):
        return self.data_type.name


class CanDataConvert:
    def __init__(self):
        pass

    @staticmethod
    def convert(recv_msg) -> int:
        data_type = recv_msg.data[DATA_TYPE_INDEX]
        try:
            handler = getattr(
                CalculateData,
                CanDataType(data_type).name.lower()
            )
            return handler(recv_msg.data)
        except AttributeError:
            raise NotSupportedDataTypeException
        except Exception as e:
            print('error occur : ', e)


# cal fef https://www.sciencedirect.com/science/article/pii/S2352484719308649
# https://stackoverflow.com/questions/44794181/fuel-consumption-and-mileage-from-obd2-port-parameters
class CalculateData:
    maf = 0
    speed = 0
    present_fuel_efficiency = 0
    average_fuel_efficiency = 0
    count = 0
    avg_buf = 0

    def __init__(self):
        pass

    @classmethod
    def average_fuel_efficiency(cls, recv_msg) -> float:
        cls.avg_buf += cls.present_fuel_efficiency
        cls.count += 1
        cls.average_fuel_efficiency = round(cls.avg_buf / cls.count, 2)
        return cls.average_fuel_efficiency

    @classmethod
    def short_term_fuel_efficiency(cls, recv_msg) -> float:
        cls.present_fuel_efficiency = round(
            cls.speed * (1 / 3600) * (1 / cls.maf) * 14.7 * 710, 2
        )
        return cls.present_fuel_efficiency

    @staticmethod
    def oxygen_sensor(recv_msg) -> float:
        # we can make two data. first one is ratio, the other is mA
        return round((256 * recv_msg[3] + recv_msg[4]) * (2 / 65536), 2)

    @staticmethod
    def intake_manifold_absolute_pressure(recv_msg) -> int:
        return recv_msg[3]

    @classmethod
    def maf_sensor(cls, recv_msg) -> float:
        cal = round((recv_msg[3] * 256 + recv_msg[4]) / 100, 2)
        cls.maf = cal
        return cal

    @staticmethod
    def engine_load(recv_msg) -> float:
        return round((100 / 255) * recv_msg[3], 2)

    @staticmethod
    def engine_rpm(recv_msg) -> float:
        return round(((recv_msg[3] * 256) + recv_msg[4]) / 4, 2)

    @classmethod
    def vehicle_speed(cls, recv_msg) -> int:
        cls.speed = recv_msg[3]
        return recv_msg[3]

    @staticmethod
    def throttle(recv_msg) -> float:
        return round((recv_msg[3] * 100) / 255, 2)

    @staticmethod
    def short_fuel_trim_bank(recv_msg) -> float:
        return round(((100 / 128) * recv_msg[3]) - 100, 2)

    @staticmethod
    def long_fuel_trim_bank(recv_msg) -> float:
        return round(((100 / 128) * recv_msg[3]) - 100, 2)

    @staticmethod
    def intake_air_temperature(recv_msg) -> int:
        return recv_msg[3] - 40

    @staticmethod
    def throttle_position(recv_msg) -> float:
        return round((100 / 256) * recv_msg[3], 2)

    @staticmethod
    def engine_runtime(recv_msg) -> int:
        return 256 * recv_msg[3] + recv_msg[4]

    @staticmethod
    def traveled_distance(recv_msg) -> int:
        return 256 * recv_msg[3] + recv_msg[4]

    @staticmethod
    def fuel_tank_level(recv_msg) -> float:
        return round((100 / 255) * recv_msg[3], 2)

    @staticmethod
    def ambient_air_temperature(recv_msg) -> int:
        return recv_msg[3] - 40


if __name__ == '__main__':
    msg1 = CanRequestMessage(CanDataType.ENGINE_LOAD)
    msg2 = CanRequestMessage(CanDataType.ENGINE_COOLANT_TEMP)
    print(msg1, msg2)
