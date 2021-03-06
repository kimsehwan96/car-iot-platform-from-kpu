import os
import time
import csv
import json
from datetime import datetime, timezone, timedelta
# from .base_dispatcher import BaseDispatcher
from _thread import start_new_thread
from abc import ABCMeta, abstractmethod
from typing import List


class BaseDispatcher(metaclass=ABCMeta):
    """
    받은 데이터를 각 용도에 맞게 consume 할 소비자 클래스의 베이스 클래스
    """

    def __init__(self):
        pass

    def run(self, data: str):
        start_new_thread(self.relay, (data,))

    @abstractmethod
    def relay(self, data):
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
        self._prev_min_dt = None
        self._cur_min_dt = None

    @staticmethod
    def convert_timestamp_to_datetime(timestamp) -> datetime:
        dt = datetime.fromtimestamp(timestamp, timezone.utc)
        return datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, tzinfo=timezone.utc)

    @staticmethod
    def merge_values_timestamp(data: dict) -> List[float or int]:
        values = data.get('values')
        timestamp = data.get('timestamp')
        values.append(timestamp)
        return values

    def _prepare_min_file_name(self, minute_dt: datetime) -> str:
        """
        주어진 분에 해당하는 dt 객체를 사용하여
        데이터 저장할 공간에 디렉터리 생성 & csv 파일명 생성
        리턴 : csv 파일명
        """
        now_dir = []
        now_dir.extend(map(lambda x: str(getattr(minute_dt, x)).zfill(2), ['year', 'month', 'day', 'hour', 'minute']))
        now_dir_path = '/'.join(now_dir)
        self.local_dirpath = os.path.join(LOCAL_DATA_PATH, now_dir_path)
        try:
            os.makedirs(self.local_dirpath, exist_ok=True)
        except Exception as e:
            print('Unexpected Error occured in prepare file :', e)
        return '{}.csv'.format(minute_dt.strftime('%Y-%m-%dT%H:%M:00Z'))

    def is_min_changes(self) -> bool:
        td = self._cur_min_dt - self._prev_min_dt
        if td.seconds >= 60:
            return True
        self._prev_min_dt = self._cur_min_dt
        return False

    def _write_csv(self, filepath: str, data: dict) -> None:
        abs_path = os.path.join(self.local_dirpath, filepath)

        def write_row_data(is_first_write=False):
            with open(abs_path, 'a') as f:
                writer = csv.writer(f)
                if is_first_write:
                    writer.writerow(data.get('fields'))
                writer.writerow(self.merge_values_timestamp(data))

        if not os.path.exists(abs_path):
            write_row_data(is_first_write=True)
            return
        write_row_data()

    def _copy_to_s3(self, files, objects):
        pass

    def _save_and_upload(self, values):
        pass

    def relay(self, data: str):
        relayed_data = json.loads(data)
        timestamp = relayed_data.get('timestamp', time.time())
        cur_dt = self.convert_timestamp_to_datetime(timestamp)
        self._current_file_name = self._prepare_min_file_name(cur_dt)
        self._write_csv(self._current_file_name, relayed_data)


if __name__ == '__main__':
    now = time.time()
