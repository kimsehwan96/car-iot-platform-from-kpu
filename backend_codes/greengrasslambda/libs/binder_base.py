import socket

IPC_PORT = 15882 #임의 지정
IPC_IP = '127.0.0.1'
ENCODING = 'latin-1'

class BinderBaseClass:
    def __init__(self):
        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM
        )
        #LOCAL IPC는 UDP를 이용해서 하자.
        self.bind_sock() #UDP socket 바인드

    def bind_sock(self):
        self.sock.bind((IPC_IP, IPC_PORT))
