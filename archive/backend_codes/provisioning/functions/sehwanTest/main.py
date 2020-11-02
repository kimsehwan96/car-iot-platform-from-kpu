import boto3
import greengrasssdk
import json
import os
import time
import datetime
from time import sleep
from random import randint
from libs.dataGetter import TestClass
from libs.mqttPublisher import Publisher
from libs.Profiler import TestProfiler as ProfileManager
########### 구현한 클래스의 인스턴스들 생성해서 돌아가는 메인 로직 ##############
target_url = "http://kimsehwanZZang.com"
api_key = "1234"
device_id = 'kim'

pm = ProfileManager(device_id)

def handler():
    print('test plugin')


def run_local():
    profile = pm.push_profile()
    device_id = profile.get('device_id')
    field_profile = profile.get('Fields')
    opt = {'IS_LOCAL' : True}
    tc = TestClass(field_profile)
    pc = Publisher(device_id, profile, tc, option=opt)
    pc.start_threading()

def run():
    profile = pm.push_profile()
    device_id = profile.get('device_id')
    field_profile = profile.get('Fields')
    tc = TestClass(field_profile)
    pc = Publisher(device_id , profile, tc)
    pc.start_threading()

if __name__ == "__main__":
    run_local() # local 에서 테스트 할 코드, pc에 option을 로컬 런타임을 주면 오키 
else:
    run() # 디바이스에서는 이게 찔러 짐