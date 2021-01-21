import socket
import json
from time import sleep
from binder_base import BinderBaseClass

IPC_PORT = 15882 #임의 지정
IPC_IP = '127.0.0.1'
ENCODING = 'latin-1'

class Encoder:
    @staticmethod
    def convert_data(data):
        return data.encode(ENCODING)

#binder_accessor가 udp 클라이언트.
class BinderAccessor(BinderBaseClass):
    #binder_accessor는 오직 데이터 전달의 역할만 할 것.
    #플러그인에서 dict 데이터를 받아오고
    #Encoder를 통해 byte로 변환 이후 바인더에게 푸시함
    def push_data(self, data):
        encoded_data = Encoder.convert_data(data)
        #Blocking 되는지 안되는지는 확인해봐야것네
        self.sock.sendto(encoded_data, self.sock_info)

if __name__ == "__main__":
    ba = BinderAccessor(is_server=False)
    data = json.dumps({
        "test" : [
            1,
            2,
            3
        ]
    })
    while True:
        sleep(1)
        ba.push_data(data)