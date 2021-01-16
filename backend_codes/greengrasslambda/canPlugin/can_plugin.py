import can
import time
import os
from collections import deque
from threading import Thread
from time import sleep
from libs.canutil import CanDataType, CanRequestMessage, CanDataConvert
from lib.plugin import run_plugin_thread

'''data source
{
    "data_types" :[
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}
'''

class CanPlugin:
    def __init__(self, data_source:dict):
        self.data_list = data_source.get('data_types')
        self.enum_list = [ getattr(CanDataType, x) for x in self.data_list]
        self.req_messages_for_data = [getattr(CanRequestMessage(x), 'message') for x in self.enum_list]
        self.data_len = len(self.data_list)
        ## data types에 있는 데이터를 호출하기 위한 메시지들 생성

        self.recv_buffer = deque() #데이터를 받기위한 덱
        self.return_buffer = deque()
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

    def send_request(self) -> list: #return으로 데이터를 받아온다.
        # 우리가 요구한 데이터는 모두 요청 메시지를 전송한다.

        # 응답에 대한 데이터만 response를 받아야 함
        def is_valid_reply(message) -> bool:
            if message.arbitration_id != CanDataType.PID_REPLY.value:
                return False
            else:
                return True

        for message in self.req_messages_for_data:
            msg = can.Message(arbitration_id=CanDataType.PID_REQUEST, data = message, extended_id=False)
            self.bus.send(msg)
        print("message request done.")
        sleep(0.1) #잠깐 기다린다.

        while len(self.recv_buffer) < len(self.data_len): #recv 버퍼가 가득 차기 전까지 수행
            recv_data = self.bus.recv()
            if is_valid_reply(recv_data):
                self.recv_buffer.append(recv_data)
            else:
                print("Not reply data, throw away : {}".format(recv_data))
        print("message recv done.")
        #데이터를 다 받았으면 각 리스트 원소 (원소 또한 리스트)에 대해서 컨버팅 로직을 수행
        while self.recv_buffer:
            self.return_buffer.append(CanDataConvert.convert(self.recv_buffer.popleft()))
        
        return self.return_buffer
        #실제 데이터로 변환 완료됨.

        #캔 플러그인 클래스는 데이터를 실제 데이터로 변환하고, 리스트로 반환하는 역할까지만 수행


            

        


def handler():
    print('test plugin')


if __name__ == '__main__':
    data_source = {
        "data_types" :[
            "ENGINE_LOAD",
            "ENGINE_RPM",
            "VEHICLE_SPEED",
            "THROTTLE"
        ]   
    }

    canplugin = CanPlugin(data_source)
    print(canplugin.req_messages)
