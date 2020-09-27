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
        "RPM",
        "Speed",
        "Brake"
    ],
    "Payload" :[
        1000,
        2000,
        3000
    ]
}

TOPIC = os.environ.get('TOPIC_EDGE')
message_format = {
    "fields" : [
        "Rpm",
        "Speed"
    ],
    "payload" : [],
    "propety" : "K7 2019"
    #"timestamp" : time.time()
}


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