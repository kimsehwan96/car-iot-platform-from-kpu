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
        "oilStatus",
        "missionOil",
        "brakeOil"
    ]
}

TOPIC = os.environ.get('TOPIC_EDGE')


def handler():
    print('test plugin')


def run():
    tc = TestClass(TEST_JSON)
    pc = Publisher('K3' , TEST_JSON, tc)
    pc.start_threading()


if __name__ == "__main__":
    run()
else:
    run()