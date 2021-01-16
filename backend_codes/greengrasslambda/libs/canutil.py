from enum import Enum

#CAN 데이터는 특정 PID 가 지정되어있음
# refer to  : https://en.wikipedia.org/wiki/OBD-II_PIDs
# 차종별, 차량 메이커별로 다를 수 있으니 우선 테스트부터 진행
# refer to : https://github.com/skpang/PiCAN-Python-examples/blob/master/obdii_logger.py

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
    def __init__(self, data_type: CanDataType):
        self.data_type = data_type #ENUM
        self.message = [0x02, 
                        0x01, 
                        self.data_type.value,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x00, 
                        0x00] #this is can data format.

# req = CanRequestMessage(CanDataType.THROTTLE).message
# req.message <- we should send this.

class CanDataConvert: #데이터 컨버팅할 스태틱 메서드들 생성
    def __init__(self):
        pass
    # message의 3번째 데이터(인덱스2)가  데이터 타입을 갖고있음
    @staticmethod
    def convert(recv_msg: list):
        data_type = recv_msg.data[2] # 0x17 과 같은 hex.

class CalculateData:

    @staticmethod
    def engine_coolant_temp(recv_msg):
        return recv_msg[3] - 40

    @staticmethod
    def engine_rpm(recv_msg):
        return round(((recv_msg.data[3]*256) + recv_msg.data[4]))

    @staticmethod
    def vehicle_speed(recv_msg):
        return recv_msg[3]
    
    @staticmethod
    def throttle(recv_msg):
        return round((recv_msg[3] * 100) /255)

    @staticmethod
    def more_loigcs_below(recv_msg):
        pass
    # 각 데이터를 컨버팅하는 로직 필요.    

if __name__ == '__main__':
    req = CanRequestMessage(CanDataType.THROTTLE).message
    print(req)