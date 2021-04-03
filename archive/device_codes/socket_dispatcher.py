from socket import *
from base_dispatcher import BaseDispatcher

IPC_PORT = 51234
IP = "0.0.0.0"


class SocketDispatcher(BaseDispatcher):
    def __init__(self, data_list):
        super().__init__(data_list)
        self.socket = socket(AF_INET, SOCK_DGRAM)  # UDP

    def relay(self, data):
        pass
        # send data to ipc receiver
