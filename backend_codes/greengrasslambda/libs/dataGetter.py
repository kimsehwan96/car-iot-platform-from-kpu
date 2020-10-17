import abc
import traceback
import threading
import time
import can
from Profiler import TestProfiler

from random import randint
#import logging

TEST_JSON = {
    "Fields" : [
        "RPM",
        "Speed",
        "Brake"
    ]
}

profiler = TestProfiler("kim")

class GetterBaseClass(abc.ABC):

    def __init__(self, profile):
        self.profile = profile
        self.back_buffer = []
        self.front_buffer = []

    @abc.abstractmethod
    def get_data(self): 
        pass

    def __reset_buffer(self): # after push data, clear buffer
        self.front_buffer = []

    def push_data(self):
        try:
            print("this is front buffer {}".format(self.front_buffer))
            self.back_buffer = self.front_buffer
            self.__reset_buffer
        except Exception as e :
            print("this is erorr", traceback.format_exc())
        return self.back_buffer # List

    def vailadte_profile(self):
        pass



class TestClass(GetterBaseClass):
    # FOR TEST.
    def get_data(self):
        self.front_buffer = [randint(1,200) for x in range(5)]

class CanClass(GetterBaseClass):

    def get_data(self):
        pass #logic here.
    
if __name__ == "__main__":
    print(profiler.push_profile())
    tc = TestClass(TEST_JSON)
    tc.get_data()
    print(tc.push_data())


