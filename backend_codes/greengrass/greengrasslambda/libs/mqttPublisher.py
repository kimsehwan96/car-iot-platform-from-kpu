import boto3
import greengrasssdk
import json
import os
import time
import datetime
import threading
from util import get_publish_topic
from datetime import datetime, timedelta
from dataGetter import TestClass

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


class Publisher:
    def __init__(self, device_id, profile, pluginCls, option = {}) :
        self.device_id = device_id
        self.profile = profile
        self.publish_topic = get_publish_topic() # edge/{groupName}/data/raw
        self.send_buffer = []
        try:
            self.mqtt_client = greengrasssdk.client('iot-data')
        except Exception as e:
            print("error occured when make iot client {}".format(e))
        self.pluginCls = pluginCls

    def get_raw_data(self):
        self.pluginCls.get_data()
        self.send_buffer = self.pluginCls.push_data()

    def reset_buffer(self):
        self.send_buffer = []

    def make_payload(self):
        payload = {}

        payload = {
            'data' : self.send_buffer,
            'timestamp' : time.time()
        }

        self.reset_buffer()

        return payload

    def get__topic(self):
        return get_publish_topic()

    def publising_data(self, data):
        pass

    def start_threading(self):
        t = threading.Timer(1.0, self.start_threading)
        t. start()
        
        self.get_raw_data()
        message = {} # reset message
        message = {
            'device_id' : self.device_id,
            'payload' : self.make_payload()
        }
        if message.get('payload') == None:
            print("error occured , there is no data")
        else:
            pass

        print(message)

        try:
            self.mqtt_client.publish(
                topic = self.publish_topic,
                payload = json.dumps(message)
            )
        except Exception as e:
            print("publishing error occured as {}".format(e))


# mqtt Publisher 클래스에서는 플러그인(캔통신 클래스화 코드)으로부터 데이터를 수집
# 데이터에 timestamp 달아주기
# 데이터 mqtt 퍼블리싱의 역할을 할 예정이다.


# 아래는 로컬 테스트 코드

if __name__ == "__main__":
    tc = TestClass(TEST_JSON)
    pc = Publisher('hello', TEST_JSON, tc)
    pc.start_threading()