import boto3
import os
import abc
import datetime
import time

BUCKET_NAME = os.environ.get('RAW_DATA_BUCKET_NAME', 'sehwan-an2-edge-dev-rawdata')
DEVICE_ID = os.environ.get('AWS_THING_NAME', 'test-group_Core')

s3 = boto3.client('s3')

class BaseStatClass(abc.ABC):

    def __init__(self):
        self.raw_data_bucket_name = BUCKET_NAME
        self.device_id = DEVICE_ID
        # temp dt
        self.dt = datetime.datetime.fromtimestamp(time.time())
        self.data_count = 0
        self.fields = self.get_fields()

    def get_fields(self):
        return [
            'timestamp',
            'rpm',
            'spedd',
            'brake',
            'oilTemp',
            'oilStatus'
        ]

    @abc.abstractmethod
    def make_stat(self):
        pass

    @abc.abstractmethod
    def count_data_num(self):
        #TODO:
        # here some logics
        return self.data_count
    # 총 몇개의 데이터를 순회할지 리턴하기.

    # 해당 시간대의 dt 중 min을 0부터 59까지 순회하고
    # 없는 것들은 예외처리를 해야 한다.
    def get_rawdata_from_s3(self):
        for i in range(self.data_count):
            obj = s3.get_object(
                Bucket = self.raw_data_bucket_name,
                Key = '{}/rawdata_{}.csv'.format(self.device_id, self.dt.strftime('%Y-%m-%d-%H-%M')) #key를 어떻게 순회할지
            # Key는 순회하면서 1시간 단위의 모든 데이터를 수집하고..
            # key range 리스트가 있으면 좋겠다.
            # ex : test-group_Core/rawdata_2020-09-30-22-00 부터, 22-59 까지 시간단위 평균은 00 ~ 59까지.
            )
            raw_data = obj.get('Body').read().decode('utf-8') #?? 테스트 해야 됨
            # raw data의 맨 첫번째 열은 필드 명이다.
            