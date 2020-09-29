import csv
import os
import datetime
import time
import threading

LOCAL_DATA_STORE_PATH = os.environ.get('LOCAL_DATA_STORE_PATH', '/rawcar/rawdata') # 원본 데이터를 저장할 디바이스 상의 경로.
# 테스트 코드는 현재 경로에다 저장할래요.

#TODO: 1. dataGetter 하는 클래스로부터 데이터를 전달 받고, profile 상의 필드와 데이터를 매칭시켜서 csv 파일로 저장

class Storer:
    def __init__(self):
        pass

    def making_csv(self):
        pass

    def save_csv(self):
        pass

    def relay_to_s3(self):
        pass

    def start_thread(self):
        pass

    