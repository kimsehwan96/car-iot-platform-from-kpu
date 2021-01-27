import os
import sys
import json
import threading
import traceback
import socket
import boto3
from time import sleep
from _thread import start_new_thread
from libs.binder_base import BinderBaseClass
# from libs.util import 

class Binder(BinderBaseClass):
    def process_data(self):
        #dispatching & process.
        pass


def hanlder(request, context):
    pass

if __name__ == "__main__":
    b = Binder(is_server=True)
    while True:
        recv = b.get_data()
        print(recv) #string type data. we can publish this data
        sleep(1)