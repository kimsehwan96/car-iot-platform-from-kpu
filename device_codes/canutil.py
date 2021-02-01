from enum import Enum

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

    PID_REQUEST = 0x7DF
    PID_REPLY = 0x7E8
    
class CanRequestMessage:

    def __str__(self):
        return "{}".format(self.message)

    def __init__(self, data_type: CanDataType) -> None:
        self.data_type = data_type #ENUM
        self.message = [0x02, 
                        0x01, 
                        self.data_type.value,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x00, 
                        0x00] 

class CanDataConvert: 
    @staticmethod
    def convert(recv_msg: list) -> int:
        data_type = recv_msg.data[2] # 0x17 과 같은 hex.
        try:
            hanlder = getattr(CalculateData, CanDataType(data_type).name.lower()) #핸들러를 갖고옴
            return hanlder(recv_msg)
        except AttributeError as e:
            print("there is no data type like that..")
            return 0

class CalculateData:

    @staticmethod
    def engine_coolant_temp(recv_msg)->int:
        return recv_msg[3] - 40

    @staticmethod
    def engine_load(recv_msg):
        return round((100/255) * recv_msg[3], 2)

    @staticmethod
    def engine_rpm(recv_msg):
        return round(((recv_msg.data[3]*256) + recv_msg.data[4]), 2)

    @staticmethod
    def vehicle_speed(recv_msg):
        return recv_msg[3]
    
    @staticmethod
    def throttle(recv_msg):
        return round((recv_msg[3] * 100) /255 , 2)

    @staticmethod
    def fuel_trim_bank(recv_msg):
        return round(((100/128) * recv_msg[3]) - 100 , 2)
    
    @staticmethod
    def intake_air_temperature(recv_msg):
        return recv_msg[3] - 40
    
    @staticmethod
    def throttle_position(recv_msg):
        return round((100/256) * recv_msg[3], 2)
    
    @staticmethod
    def engine_runtime(recv_msg):
        return 256 * recv_msg[3] + recv_msg[4]
    
    @staticmethod
    def traveled_distance(recv_msg):
        return 256 * recv_msg[3] + recv_msg[4]
    
    @staticmethod
    def fuel_tank_level(recv_msg):
        return round((100/255) * recv_msg[3], 2)
    
    @staticmethod
    def ambient_air_temperature(recv_msg):
        return recv_msg[3] - 40


if __name__ == '__main__':
    msg1 = CanRequestMessage(CanDataType.ENGINE_LOAD)
    msg2 = CanRequestMessage(CanDataType.ENGINE_COOLANT_TEMP)
    print(msg1, msg2)
    