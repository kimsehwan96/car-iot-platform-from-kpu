import os
import sys
import json
import threading
import traceback
import socket
from time import sleep
from _thread import start_new_thread
from .libs.binder_base import BinderBaseClass

class Binder(BinderBaseClass):
    def get_data(self):
        pass
    
    def process_data(self):
        #dispatching & process.
        pass

def handler(event, context):
    pass