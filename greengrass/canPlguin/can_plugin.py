import can
import subprocess
from libs import util
from libs.plugin import run_plugin_thread
from libs.ipc_helper import IpcHelper
from collections import deque
from time import sleep
from canutil import CanDataType, CanRequestMessage, CanDataConvert
from libs.base_plugin import BasePlugin

TOPIC = util.get_ipc_topic()

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

OPTION = {
    'channel': 'can0',
    'busType': 'socketcan_native'
}

# TODO:
# add description in Korean


class CanPlugin(BasePlugin):
    # TODO: inherite base class and refactor below methods !
    def __init__(self, fields: [str], option: dict = {}) -> None:
        super().__init__(fields, option=option)
        self.data_list = fields
        self.enum_list = [getattr(CanDataType, x) for x in self.data_list]
        self.req_messages_for_data = [getattr(CanRequestMessage(x), 'message') for x in self.enum_list]
        self.data_len = len(self.data_list)
        self.recv_buffer = deque()
        self.return_buffer = deque()
        self._channel = option.get('channel', 'can0')
        self._bus_type = option.get('busType', 'socketcan_native')
        self.bus = can.interface.Bus(channel=self._channel, bustype=self._bus_type)
        if not subprocess.check_call(['/sbin/ip', 'link', 'set', 'can0', 'up', 'type', 'can', 'bitrate', '500000']):
            print('failed to init can device')

    # TODO:
    # 1. set return_buffer & recv_buffer with property

    def _send_request(self) -> deque[[float]]:
        self.return_buffer.clear()

        def is_valid_reply(message) -> bool:
            if message.arbitration_id != CanDataType.PID_REPLY.value:
                return False
            else:
                return True

        for message in self.req_messages_for_data:
            msg = can.Message(arbitration_id=CanDataType.PID_REQUEST.value, data=message, extended_id=False)
            self.bus.send(msg)
        print("message request done.")
        sleep(0.1)

        while len(self.recv_buffer) < self.data_len:
            recv_data = self.bus.recv()
            if is_valid_reply(recv_data):
                self.recv_buffer.append(recv_data)
            else:
                print("Not reply data, throw away : {}".format(recv_data))
        print("message recv done.")

        while self.recv_buffer:
            self.return_buffer.append(CanDataConvert.convert(self.recv_buffer.popleft()))

        return self.return_buffer
        # deque가 리턴되며, DATA_SOURCE의 순서대로 저장이 된다

    def collect_data(self):
        self.data = self._send_request()
        print('this is bufferd data: ', self.data)


def handler(event, context):
    pass


cp = CanPlugin(TEST_FIELDS)


def run():
    run_plugin_thread(cp.entry)


if __name__ == '__main__':
    pass
else:
    run()
