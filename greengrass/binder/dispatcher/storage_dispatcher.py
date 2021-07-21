import os
import time
import csv
import json
import boto3
from datetime import datetime, timezone, timedelta
# from .base_dispatcher import BaseDispatcher
from _thread import start_new_thread
from threading import Thread
from copy import deepcopy
from abc import ABCMeta, abstractmethod
from typing import List
from libs.util import check_connected_to_internet

RAW_DATA_BUCKET = os.environ.get('RAW_DATA_BUCKET_NAME', 'kpu-gradutation-team-rawdata-dev')

try:
    if check_connected_to_internet():
        s3 = boto3.resource('s3')
    else:
        s3 = None
except Exception as e:
    print('error occured when making s3 resources.. ', e)


class BaseDispatcher(metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume 할 소비자 클래스의 베이스 클래스
    """

    def __init__(self) -> None:
        pass

    def run(self, data: str) -> None:
        start_new_thread(self.relay, (data,))

    @abstractmethod
    def relay(self, data) -> None:
        """
        각 클래스 구현부에서 달라지는 메서드임.
        """
        raise NotImplementedError("추상 메서드입니다.")


"""
relay 되는 데이터의 형태

{'fields':
    [
        'engine_load',
        'engine_coolant_temp',
        'engine_rpm',
        'vehicle_speed',
        'maf_sensor',
        'o2_voltage',
        'throttle',
        'short_fuel_trim_bank',
        'long_fuel_trim_bank',
        'intake_air_temperature',
        'engine_runtime',
        'traveled_distance',
        'fuel_tank_level',
        'ambient_air_temperature',
        'engine_oil_temperature',
        'transmission_actual_gear'
    ],
    'values': [40, 64, 13, 40, 99, 99, 36, 94, 6, 6, 84, 47, 86, 20, 61, 2],
    'timestamp': 1618150407.851798
}
"""

LOCAL_DATA_PATH = f'/kpu/rawdata'


class StorageDispatcher(BaseDispatcher):
    """
    StorageDispatcher
    csv 파일을 1분단위로 저장하는 디스패쳐임
    /kpu/rawdata/2020/04/29/00/01  과 같이 디렉터리 구조 안에 파일을 저장 할 예정임
    이 파일은 S3 특정 버킷에도 업로드 할 것임
    """

    def __init__(self) -> None:
        if not os.path.exists(LOCAL_DATA_PATH):
            os.makedirs(LOCAL_DATA_PATH)
        self._current_file_name = None
        self._cur_dt = None
        self._prev_dt = None
        self._upload_file_path = None  # /kpu/rawdata/2021/05/01/05/06/2021-05-01:05:06:00Z.csv

    @staticmethod
    def convert_timestamp_to_datetime(timestamp) -> datetime:
        dt = datetime.fromtimestamp(timestamp, timezone.utc)
        return datetime(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            tzinfo=timezone.utc
        )

    @staticmethod
    def merge_values_timestamp(data: dict) -> List[float or int]:
        values = data.get('values')
        timestamp = data.get('timestamp')
        values.append(timestamp)
        return values

    def _prepare_min_file_dir_name(self, minute_dt: datetime) -> str:
        """
        주어진 분에 해당하는 dt 객체를 사용하여
        데이터 저장할 공간에 디렉터리 생성
        """
        now_dir = []
        now_dir.extend(
            map(
                lambda x: str(getattr(minute_dt, x)).zfill(2),
                ['year', 'month', 'day', 'hour', 'minute']
            )
        )
        now_dir_path = '/'.join(now_dir)  # 2021/05/01/22/01

        return os.path.join(LOCAL_DATA_PATH, now_dir_path)  # /kpu/rawdata/2021/05/01/05/06

    def _prepare_min_file_name(self, minute_dt: datetime) -> str:
        """
        dt 객체를 입력받아 현재 분에 해당하는 파일명을 생성함.
        리턴 : '2021-05-01:05:06:00Z.csv'
        """
        return '{}.csv'.format(minute_dt.strftime('%Y-%m-%dT%H:%M:00Z'))

    def _write_csv(self, filepath: str, data: dict) -> None:
        def merge_fields_and_timestamp(fields: list) -> list:
            fields.append('timestamp')
            return fields

        def write_row_data(is_first_write=False):
            with open(filepath, 'a') as f:
                writer = csv.writer(f)
                if is_first_write:
                    writer.writerow(merge_fields_and_timestamp(data.get('fields')))
                writer.writerow(self.merge_values_timestamp(data))

        if not os.path.exists(filepath):
            write_row_data(is_first_write=True)
            return
        write_row_data()

    def _copy_to_s3(self, files: List[str], objects: List[str]) -> None:
        """
        1분마다 데이터 업로드를 수행할 스레드가 호출하는 함수. 로컬에있는 파일을 S3에 업로드하는 코드
        """
        global s3
        if s3:
            for f, o in zip(files, objects):
                try:
                    s3.meta.client.upload_file(f, RAW_DATA_BUCKET, o)
                except Exception as e:
                    print('error occured when upload local file {}'.format(e))
            print('s3 upload completed')
        else:
            try:
                s3 = boto3.resource('s3')
                print("try to make s3 resource")
            except Exception as e:
                print("retry make s3 resource failed {}".format(e))
                s3 = None
            print("no internet connection !!")

    def run_upload_thread(self, filepath: str) -> None:
        """
        1분마다 데이터 업로드를 수행할 스레드
        """
        try:
            print('-' * 50)
            print('upload thread called!')
            Thread(target=self._copy_to_s3,
                   args=deepcopy(([filepath],
                                  [filepath]))).start()
        except Exception as e:
            print('-' * 50)
            print('upload thread error occcured ', e)

    def relay(self, data: str) -> None:
        relayed_data = json.loads(data)
        timestamp = relayed_data.get('timestamp', time.time())
        cur_dt = self.convert_timestamp_to_datetime(timestamp)
        if not self._cur_dt:  # 최초에 cur_dt가 없을 때 dt 설정
            self._cur_dt = cur_dt
        if (cur_dt - self._cur_dt).seconds >= 60:
            # 시간이 바뀐것이기 때문에 업로드 로직을 수행함
            print('-' * 100)
            print('time changed !')
            upload_file_path = os.path.join(
                self._prepare_min_file_dir_name(self._cur_dt),
                self._prepare_min_file_name(self._cur_dt)
            )
            self.run_upload_thread(upload_file_path)
            # 시간이 바뀐것을 반영하기 위해 self._cur_dt 업데이트
            self._cur_dt = cur_dt
        try:
            os.makedirs(self._prepare_min_file_dir_name(self._cur_dt), exist_ok=True)
        except Exception as e:
            print('Unexpected Error occured in prepare file :', e)
        self._current_file_name = self._prepare_min_file_name(self._cur_dt)
        self._write_csv(
            os.path.join(
                self._prepare_min_file_dir_name(self._cur_dt),
                self._prepare_min_file_name(self._cur_dt)
            )
            , relayed_data
        )


if __name__ == '__main__':
    now = time.time()
