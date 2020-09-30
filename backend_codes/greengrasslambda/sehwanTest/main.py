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

TEST_JSON = {
    "Fields" : [
        "rpm",
        "speed",
        "brake",
        "oilTemp",
        "oilStatus"
    ]
}
def handler():
    print('test plugin')


def run_local():
    opt = {'IS_LOCAL' : True}
    tc = TestClass(TEST_JSON)
    pc = Publisher('K3' , TEST_JSON, tc, option=opt)
    pc.start_threading()

def run():
    tc = TestClass(TEST_JSON)
    pc = Publisher('K3' , TEST_JSON, tc)
    pc.start_threading()

if __name__ == "__main__":
    run_local() # local 에서 테스트 할 코드, pc에 option을 로컬 런타임을 주면 오키 
else:
    run() # 디바이스에서는 이게 찔러 짐