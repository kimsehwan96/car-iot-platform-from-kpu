import boto3
import os
import csv
import datetime
import time
import threading
from .util import timestamp_to_datetime

LOCAL_DATA_STORE_PATH = os.environ.get('LOCAL_DATA_STORE_PATH', '/rawcar/rawdata') # 원본 데이터를 저장할 디바이스 상의 경로.
# 테스트 코드는 현재 경로에다 저장할래요.

#TODO: 1. dataGetter 하는 클래스로부터 데이터를 전달 받고, profile 상의 필드와 데이터를 매칭시켜서 csv 파일로 저장

#TODO: S3 에 1분간 저장된 원본 데이터를 저장하는 로직이 들어 갈 예정
DEVICE_ID = os.environ.get("AWS_IOT_THING_NAME", 'test_id')
s3 = boto3.resource('s3')


class BaseStorageManager:

    def __init__(self, device_id):
        self.payload = {}
        self.device_id = device_id
        self.fields = []
        self.data  =  []
        self.timestamp = None 
    
    def get_payload(self):
        return self.payload

    def failed_save(self):
        pass

    def check_payload(self, payload):
        if payload.get('Fields') & payload.get('data') & payload.get('timestamp'):
            return True
        else:
            print("there is missing data in data {}".format(payload))
            return False

    def relay(self, data):
        if self.payload:
            self.reset_buffers()
            if self.check_payload(data):
                self.payload = data
                self.fields = self.payload.get('Fields')
                self.data = self.payload.get('data')
                self.timestamp = self.payload.get('timestamp')
            else:
                print("error occured")
        else:
            if self.check_payload(data):
                self.payload = data
                self.fields = self.payload.get('Fields')
                self.data = self.payload.get('data')
                self.timestamp = self.payload.get('timestamp')
            else:
                print("errror occured")

    def reset_buffers(self):
        self.payload = {}
        self.fields = []
        self.data = []

    def make_csv(self):
        pass

    #TODO: datetime 오브젝트에서, 기준이 되는 minutes를 정하고, 다음 minutes가 되기 전까지의
    # 데이터를 배열로 저장, csv에 쓰면 될 듯 하다.
    # 포멧
    # 기준 필드명 필드명 필드명 필드명
    # 시간   1   2    3    4
    # 시간   9   0    2    1
    # 시간   2   1    3    4
    # 시간   4   2    1    3


class LocalStorageManager(BaseStorageManager):
    pass


if __name__ == "__main__":
    pass