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
from libs.api_tool import ProfileManager

TEST_JSON = {
    "Fields" : [
        "rpm",
        "speed",
        "brake",
        "oilTemp",
        "oilStatus"
    ]
}

target_url = "http://kimsehwanZZang.com"
api_key = "1234"

pm = ProfileManager(target_url, api_key)

def handler():
    print('test plugin')


def run_local():
    profile = pm.get_profile()
    device_id = profile.get('device_id')
    field_profile = profile.get('Fields')
    opt = {'IS_LOCAL' : True}
    tc = TestClass(field_profile)
    pc = Publisher(device_id, field_profile, tc, option=opt)
    pc.start_threading()

def run():
    profile = pm.get_profile()
    device_id = profile.get('device_id')
    field_profile = profile.get('Fields')
    tc = TestClass(field_profile)
    pc = Publisher(device_id , field_profile, tc)
    pc.start_threading()

if __name__ == "__main__":
    run_local() # local 에서 테스트 할 코드, pc에 option을 로컬 런타임을 주면 오키 
else:
    run() # 디바이스에서는 이게 찔러 짐