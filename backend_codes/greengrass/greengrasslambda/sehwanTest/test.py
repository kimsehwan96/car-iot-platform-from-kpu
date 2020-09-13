import boto3
import greengrasssdk
import json
import os
import time
import datetime
from time import sleep
from random import randint

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

#return json.dumps(message)
def fill_data(message: dict):
    if message_format.get('payload') != []:
        message_format['payload'] = []
    else:
        pass
    for v in message.get('fields'):
        message['payload'].append(randint(5,5000))
    message['timestamp'] = time.time()

    return json.dumps(message)        

def run():
    try:
        print("try to make gg cleint")
        client = greengrasssdk.client('iot-data')
    except Exception as e:
        print("error : {}".format(e))
    while True:
        sleep(1)
        print("this is test logic !!") #this can view in log files.
        client.publish(
            topic=TOPIC,
            payload=fill_data(message_format)
        )
        print("data was sent")

if __name__ == "__main__":
    pass
else:
    run()