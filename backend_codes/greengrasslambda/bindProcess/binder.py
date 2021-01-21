import os
import sys
import json
import threading
import traceback
import socket
from time import sleep
from _thread import start_new_thread
from libs.binder_base import BinderBaseClass

class Binder(BinderBaseClass):
    def get_data(self):
        return self.sock.recvfrom(4096)[0].decode('latin-1')
    
    def process_data(self):
        #dispatching & process.
        pass

def handler(event, context):
    pass


if __name__ == "__main__":
    b = Binder(is_server=True)
    while True:
        print(b.get_data())
        sleep(1)