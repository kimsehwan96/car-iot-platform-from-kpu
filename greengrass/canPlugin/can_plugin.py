mport can
import subprocess
from libs import util
from libs.plugin import run_plugin_thread
from collections import deque
from time import sleep
from canutil import CanDataType, CanRequestMessage, CanDataConvert
from libs.base_plugin import BasePlugin
from typing import List

TOPIC = util.get_ipc_topic()

TEST_FIELDS = [
    'engine_load', #o
    'engine_coolant_temp', #x
    'engine_rpm', # o
    'vehicle_speed', #o
#    'maf_sensor' #x static 메소드도 없음 !
#    'o2_voltage', #x
    'throttle', #o
    'short_fuel_trim_bank', #o
#    'long_fuel_trim_bank' #x
 #   'intake_air_temperature', #
    'engine_runtime', #o
    'traveled_distance', #o
    'fuel_tank_level', #o
    'ambient_air_temperature' #o
#    'engine_oil_temperature', #x
#    'transmission_actual_gear' #x
]

OPTION = {
    'channel': 'can0',
    'busType': 'socketcan_native'
}

INIT_COMMAND = '/sbin/ip link set can0 up type can bitrate 500000'


class SocketCanInitFailedException(Exception):
    def __init__(self):
        super().__init__('소켓 캔 초기화 패')


# TODO:
# add description in Korean


class CanPlugin(BasePlugin):
    # TODO: inherite base class and refactor below methods !
    def __init__(self, fields: List[str], option=None) -> None:
        super().__init__(fields, option=option)
        self.data_list = [x.upper() for x in fields]
        self.enum_list = [
            getattr(CanDataType, x) for x in self.data_list
        ]
        self.req_messages_for_data = [
            getattr(CanRequestMessage(x), 'message') for x in self.enum_list
        ]
        self.data_len = len(self.data_list)
        self.recv_buffer = deque()
        self.return_buffer = deque()
        self._channel = option.get('channel', 'can0')
        self._bus_type = option.get('busType', 'socketcan_native')
        # self._init_can()
        self.bus = can.interface.Bus(channel=self._channel, bustype=self._bus_type)

    def _init_can(self) -> None:
        if not subprocess.check_call(INIT_COMMAND.split()):
            print('failed to init can device')
            self._can_ready = False
        else:
            self._can_ready = True
            print('init success')

    # TODO:
    # 1. set return_buffer & recv_buffer with property

    def _send_request(self):
        self.return_buffer.clear()
        print("버퍼 초기화")
        def is_valid_reply(message) -> bool:
            if message.arbitration_id != CanDataType.PID_REPLY.value:
                return False
            else:
                return True
        for message in self.req_messages_for_data:
            msg = can.Message(arbitration_id=CanDataType.PID_REQUEST.value, data = message, extended_id=False)
 #           print("this is will send can msg " , msg)
            self.bus.send(msg)
            sleep(0.01)
            while True:
                recv_data = self.bus.recv()
                if is_valid_reply(recv_data):
                    self.recv_buffer.append(recv_data)
                    print('catch data : ', recv_data)
                    break
                print("Not reply data, throw away : {}".format(recv_data))
                sleep(0.01)
                continue
        print("message recv done.")
        while len(self.recv_buffer) < self.data_len:
            recv_data = self.bus.recv()
            print('데이터 받음 ,', recv_data)
            if is_valid_reply(recv_data):
                self.recv_buffer.append(recv_data)
            else:
                print("Not reply data, throw away : {}".format(recv_data))
        print('-'*100)
        print("message recv done.")
        print("this buffer will be processed !!!!!!!!! ", self.recv_buffer)
        print('-'*100)
        while self.recv_buffer:
            self.return_buffer.append(
                CanDataConvert.convert(
                    self.recv_buffer.popleft()
                )
            )

        return self.return_buffer
        # deque가 리턴되며, DATA_SOURCE의 순서대로 저장이 된다

    def collect_data(self) -> None:
        try:
            self.data = list(self._send_request())
            print('this is bufferd data: ', self.data)
        except Exception as e:
            print('error occured when collect data ', e)


def handler(event, context) -> None:
    pass


try:
    cp = CanPlugin(TEST_FIELDS, OPTION)
except Exception as e:
    print('failed to make can plugin :', e)


def run():
    run_plugin_thread(cp.entry)


if __name__ == '__main__':
    pass
else:
    run()
