import boto3
import os
import csv
import datetime
import time
import threading
from .util import timestamp_to_datetime, get_year, get_month, get_day, get_hour, get_min

LOCAL_DATA_STORE_PATH = os.environ.get('LOCAL_DATA_STORE_PATH', '/rawcar/rawdata') # 원본 데이터를 저장할 디바이스 상의 경로.
# 테스트 코드는 현재 경로에다 저장할래요.

#TODO: 1. dataGetter 하는 클래스로부터 데이터를 전달 받고, profile 상의 필드와 데이터를 매칭시켜서 csv 파일로 저장

#TODO: S3 에 1분간 저장된 원본 데이터를 저장하는 로직이 들어 갈 예정
S3_SAVE_BUCKET = os.environ.get('S3_SAVE_BUCKET', 'sehwan-an2-edge-dev-rawdata')
DEVICE_ID = os.environ.get("AWS_IOT_THING_NAME", 'test_id')
s3 = boto3.resource('s3')


class BaseStorageManager:

    def __init__(self, device_id):
        self.payload = {}
        self.device_id = device_id
        self.fields = []
        self.data  =  []
        self.timestamp = None 
        self.csv_buffer = [] #iter 객체 생성. csv파일을 위해.
        self.base_dt_min = 0
    
    def get_payload(self):
        return self.payload

    def failed_save(self):
        pass

    def check_payload(self, payload):
        if (payload.get('Fields') != None) & (payload.get('data') != None) & (payload.get('timestamp') !=None):
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
                print("this is relayed payload {}".format(self.payload))
            else:
                print("error occured")
        else:
            if self.check_payload(data):
                self.payload = data
                self.fields = self.payload.get('Fields')
                self.data = self.payload.get('data')
                self.timestamp = self.payload.get('timestamp')
                print("this is relayed payload {}".format(self.payload))
            else:
                print("errror occured")

    def reset_buffers(self):
        self.payload = {}
        self.fields = []
        self.data = []
        print("reset buffers excuted")
    
    def reset_csv_buffer(self):
        self.csv_buffer = [] 

    def merge_data(self, data):
        processed_list = []
        payload = data
        values = payload.get('data')
        timestamp = payload.get('timestamp')
        processed_list = [timestamp]
        for v in values:
            processed_list.append(v)
        dt = timestamp_to_datetime(self.timestamp)
        tmp_dt_min = get_min(dt)
        print("merge data excuted")
        print("this is csv buffer {}".format(self.csv_buffer))
        print("this is base dt min {} & this is tmp dt min {}".format(self.base_dt_min, tmp_dt_min))
        if tmp_dt_min == self.base_dt_min:
            self.csv_buffer.append(processed_list) #append 할때 변형을 해야 한다.
        else:
            self.base_dt_min = tmp_dt_min
            self.save_csv_data(self.csv_buffer)
            print("this is csv_buffer {}".format(self.csv_buffer))
            self.reset_csv_buffer()
        #TODO: tmp_dt_min과 self.base_dt_min 비교해서
        # 다르다면 1분 넘어간것이기 때문에 csv_buffer 에 계속 append된 데이터를
        # make_csv_format 호출해서 csv 파일 포맷을 만들고, csv파일을 생각해서 저장
        # dt 관련한 코드는 util.py 에 구현

    def save_csv_data(self, data):
        rows = data
        fields = ['timestamp']
        dt = timestamp_to_datetime(self.timestamp)
        dt_year = get_year(dt)
        dt_month = get_month(dt)
        dt_day = get_day(dt)
        dt_hour = get_hour(dt)
        dt_min = get_min(dt)
        fileName = 'rawdata_{}_{}_{}_{}_{}.csv'.format(dt_year, dt_month, dt_day, dt_hour, dt_min - 1)

        for v in self.fields:
            fields.append(v)
        with open (fileName, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        self.save_to_s3(fileName)
        # fields = ['timestamp', 'a' , 'b', 'c']
        # TODO: 저장된 데이터를 어떻게 S3에 넘길지 고민해보기.... 개어려워....

    def save_to_s3(self, fileName):
        s3.meta.client.upload_file(
            os.getcwd() + '/' + fileName,
            S3_SAVE_BUCKET,
            DEVICE_ID + '/' + fileName
        )
        print("save local csv file into S3 !! {}".format(fileName))

    #TODO: datetime 오브젝트에서, 기준이 되는 minutes를 정하고, 다음 minutes가 되기 전까지의
    # 데이터를 배열로 저장, csv에 쓰면 될 듯 하다.
    # 포멧
    # 기준 필드명 필드명 필드명 필드명
    # 시간   1   2    3    4
    # 시간   9   0    2    1
    # 시간   2   1    3    4
    # 시간   4   2    1    3
# 개어려워..

class LocalStorageManager(BaseStorageManager):
    pass


if __name__ == "__main__":
    pass