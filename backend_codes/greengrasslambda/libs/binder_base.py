import socket

IPC_PORT = 15882 #임의 지정
IPC_IP = '127.0.0.1'
ENCODING = 'latin-1'

class BinderBaseClass:
    def __init__(self, is_server = False): #Binder는 True, Accesor는 False로 생성.
        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM
        )
        self.sock_info = (IPC_IP, IPC_PORT)
        #LOCAL IPC는 UDP를 이용해서 하자.
        if is_server:
            self.bind_sock() #UDP socket 바인드
        else:
            pass

    def bind_sock(self):
        self.sock.bind((IPC_IP, IPC_PORT))

    def push_data(self):
        pass

    def get_data(self):
        return self.sock.recvfrom(4096)[0].decode(ENCODING)
