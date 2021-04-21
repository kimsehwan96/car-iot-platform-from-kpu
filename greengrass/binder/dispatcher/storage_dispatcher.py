# TODO:
# Make csv files
# Save csv file in local
# Upload csv file to S3
import os
import time
from datetime import datetime, timezone

from .base_dispatcher import BaseDispatcher

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

LOCAL_DATA_PATH = '/kpu/rawdata'


def convert_timstamp_to_datetime(timestamp):
    dt = datetime.fromtimestamp(timestamp, timezone.utc)
    return datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, tzinfo=timezone.utc)


class StorageDispatcher(BaseDispatcher):
    def __init__(self):
        if not os.path.exists(LOCAL_DATA_PATH):
            os.makedirs(LOCAL_DATA_PATH)

    def prepare_file(self, minute_dt: datetime) -> str:
        """
        주어진 분에 해당하는 dt 객체를 사용하여
        데이터 저장할 공간에 디렉터리 생성 & csv 파일명 생성
        리턴 : csv 파일명
        """
        now_dir = []
        now_dir.extend(map(lambda x: str(getattr(minute_dt, x)).zfill(2), ['year', 'month', 'day', 'hour', 'minute']))
        now_dir_path = '/'.join(now_dir)
        local_dirpath = os.path.join(LOCAL_DATA_PATH, now_dir_path)
        try:
            os.makedirs(local_dirpath, exist_ok=True)
        except Exception as e:
            print('Unexpected Error occured in prepare file :', e)
        return '{}.csv'.format(minute_dt.strdtime('%Y-%m-%dT%H:%M:00Z'))

    def write_csv(self, filepath, data):
        pass

    def copy_to_s3(self, files, objects):
        pass

    def save_and_upload(self, values):
        pass

    def relay(self, data: str):
        pass


if __name__ == '__main__':
    now = time.time()

    now_dt = convert_timstamp_to_datetime(now)

    print(now_dt)
