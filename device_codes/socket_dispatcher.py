from socket import *
from device_codes.base_dispatcher import BaseDispatcher

IPC_PORT = 51234
IP = "0.0.0.0"

class SocketDispatcher(BaseDispatcher):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.socket = socket(AF_INET, SOCK_DGRAM) #UDP
    
    def relay(self, data):
        pass
        #send data to ipc receiver
    