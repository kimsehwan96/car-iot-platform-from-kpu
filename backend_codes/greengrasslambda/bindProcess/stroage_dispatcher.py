import os
import csv
import traceback
import sys
import shutil
import requests
import boto3 #python aws sdk
from collections import deque
from _thread import start_new_thread, allocate_lock
from datetime import datetime, timedelta, timezone
from .base_dispatcher import BaseDispatcher

def check_network(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

try:
    if check_network():
        s3 = boto3.resource('s3')
    else:
        s3 = None
except Exception as e:
    print("error occured when try  to connect internet {}".format(e))

LOCAL_RAWDATA_ROOT_PATH = os.environ.get('LOCAL_RAWDATA_ROOT_PATH', '/rawcar/edge_rawdata')
S3_SAVE_BUCKET= os.environ.get('S3_SAVE_BUCKET', 'kpu-car-iot-rawdata')

MERGED_KEY_FIELDS = 'fields'
MERGED_KEY_VALUES = 'values'

class StorageDispatcher(BaseDispatcher):
    def __init__(self, edge_id, target):
        super().__init__(edge_id, target)
        self.queue = deque([])
        self.minute = None
        self.lock_upload = allocate_lock()

    def _merge(self):
        merged_data = {'edgeId': self.edge_id, MERGED_KEY_FIELDS: [], MERGED_KEY_VALUES: []}

        if not self.queue:
            return merged_data
        
        merged_data[MERGED_KEY_FIELDS] = self.queue[0][MERGED_KEY_FIELDS]
        base_timestamp = self.queue[0][MERGED_KEY_VALUES][0][0]
        base_dt = datetime.fromtimestamp(base_timestamp, timezone.utc)

        #TODO: check netx datetime delta. 
        # merging data queue login with Best time complexity !!

    def write_csv(self, filepath, data):
        with open(filepath, 'w')  as f:
            cf = csv.writer(f)
            cf.writerow(data[MERGED_KEY_FIELDS])
            cf.writerows(data[MERGED_KEY_VALUES])
            return
    
    def copy_to_s3(self, files, objects):
        global s3
        if not self.lock_upload.acquire(0): #업로드 로직에 대해 락을 걸어서 이전 업로드가 끝나지 않았을 경우 자원 해제를 기다림
            print("previous upload have not been completed")
            return
        if s3:
            for f, o in zip(files, objects):
                s3.meta.client.upload_file(f, S3_SAVE_BUCKET, o)
            print("Complete upload  !")
        else:
            try:
                s3 = boto3.resources('s3')
            except Exception as e:
                s3 = None
        
        self.lock_upload.release()

    def _save(self):
        pass
        #TODO:
        #파일 저장 로직 구현 필요 !
