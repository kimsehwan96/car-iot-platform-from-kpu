import os
import json
import abc

class BaseProfiler(abc.ABC):
    def __init__(self, device_id):
        self.device_id = device_id
        self.__profile = None
    
    @abc.abstractmethod
    def get_profile(self):
        pass

    @abc.abstractmethod
    def push_profile(self):
        pass

class TestProfiler(BaseProfiler):
    # for test
    def __init__(self, device_id):
        super().__init__(device_id)
        try:
            self.get_profile() #최초에 profile 받기 위해서
        except Exception as e:
            print("error occuered when get profile from cloufd", e)
        
    def get_profile(self):
        self.__profile = {
            "device_id" : self.device_id,
            "Fields" : [
                "rpm",
                "speed",
                "brake",
                "oilTemp",
                "oilStatus"
            ]
        }
    
    def push_profile(self):
        self.get_profile()
        return self.__profile
    #here will be some api executing logics
    
if __name__ == "__main__":
    profiler = TestProfiler("kimsehwan")
    res = profiler.push_profile()
    print(res)