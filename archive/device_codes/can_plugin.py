import can
import time
import os
from collections import deque
from time import sleep
from canutil import CanDataType, CanRequestMessage, CanDataConvert

DATA_SOURCE = {
    "dataTypes": [
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}
CHANNEL = 'can0'
BUS_TYPE = 'socketcan_native'


class CanPlugin:
    def __init__(self, data_source: dict) -> None:
        self.data_list = data_source.get('dataTypes')
        self.enum_list = [getattr(CanDataType, x) for x in self.data_list]
        self.req_messages_for_data = [getattr(CanRequestMessage(x), 'message') for x in self.enum_list]
        self.data_len = len(self.data_list)
        self.recv_buffer = deque()
        self.return_buffer = deque()
        self.bus = can.interface.Bus(channel=CHANNEL, bustype=BUS_TYPE)

    def send_request(self) -> deque([float]):
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


if __name__ == '__main__':
    cp = CanPlugin(DATA_SOURCE)
    while True:
        time.sleep(1)
        print(cp.send_request())
