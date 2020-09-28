import boto3
import greengrasssdk
import json
import os
import time
import datetime
import threading
from util import timestamp_to_datetime, get_min, get_publish_topic
from datetime import datetime, timedelta
from dataGetter import TestClass
from storageManager import BaseStorageManager

TEST_JSON = {
    "Fields" : [
        "rpm",
        "speed",
        "brake",
        "oilTemp",
        "oilStatus"
    ]
}


class Publisher:
    def __init__(self, device_id, profile, pluginCls, option = {}) :
        self.device_id = device_id
        self.profile = profile # 센싱할 데이터 개수/ 필드등을 정의 할 예정임.
        self.publish_topic = get_publish_topic() # edge/{groupName}/data/raw
        self.send_buffer = []
        self.fields = self.profile.get('Fields')
        self.storageManger =BaseStorageManager('hello')
        try:
            self.mqtt_client = greengrasssdk.client('iot-data')
            print(self.mqtt_client)
        except Exception as e:
            print("error occured when make iot client {}".format(e))
        self.pluginCls = pluginCls

    def vaildating_profile(self, fields, data):
        if len(fields) == len(data):
            return True
        else:
            print("fields & data is not matching")
            print("fields :", fields, "data" , data)
            return False

    def get_raw_data(self):
        self.pluginCls.get_data()
        self.send_buffer = self.pluginCls.push_data()

    def reset_buffer(self):
        self.send_buffer = []

    def make_payload(self):

        payload = {
            'Fields' : self.fields,
            'data' : self.send_buffer,
            'timestamp' : time.time()
        }

        if self.vaildating_profile(payload.get('Fields'), payload.get('data')):
            self.reset_buffer()
            return payload
        else:
            print("there is error occured in vaildating fields & data")
            return {
                'Fields' : "Null",
                'data' : "Null",
                'timestamp' : time.time()
            }

    def get_topic(self):
        return get_publish_topic()

    def start_threading(self):
        # 1초마다 실행되는 로직
        t = threading.Timer(1.0, self.start_threading)
        t. start()
        self.get_raw_data()
        payload = {}
        payload = self.make_payload()
        self.storageManger.relay(payload)
        self.storageManger.merge_data(payload)
        message = {
            'device_id' : self.device_id,
            'payload' : payload
        }
        if message.get('payload') == None:
            print("error occured , there is no data")
        else:
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