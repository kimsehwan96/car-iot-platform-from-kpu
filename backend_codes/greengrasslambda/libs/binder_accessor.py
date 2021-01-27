import socket
import json
from time import sleep

IPC_PORT = 15882 #임의 지정
IPC_IP = '127.0.0.1'
ENCODING = 'latin-1'

class BinderAccessor:
    def __init__(self) -> None:
        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM
        )
        self.sock_info = (IPC_IP, IPC_PORT)
        #LOCAL IPC는 UDP를 이용해서 하자.
        self.bind_sock() #UDP socket 바인드

    def bind_sock(self):
        self.sock.bind((IPC_IP, IPC_PORT))

    def push_data(self, data:str) -> None:
        encoded_data = data.encode(ENCODING)
        #Blocking 되는지 안되는지는 확인해봐야것네
        self.sock.sendto(encoded_data, self.sock_info)

if __name__ == "__main__":
    ba = BinderAccessor()
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