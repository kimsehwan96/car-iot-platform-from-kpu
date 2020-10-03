# TODO: 람다를 1시간마다 invoke 하기 위한 코드
# events -> cron 스케줄 이용.

import boto3
import abc
import os
import datetime
import time

BUCKET_NAME = os.environ.get('RAW_BUCKET', 'if this texts show, Env var wasnt detectd')

def timenow_dt():
    time_now = time.time()
    dt = datetime.datetime.fromtimestamp(time_now)
    return dt
    #invoke 요청 할 당시의 datetime object
    
def handler(event, context):
    print("this lambda has invoked!! (cron test lambda)")
    print("this is BUCKET_NAME {}".format(BUCKET_NAME))

    #dt = timenow_dt()
    dt = datetime.datetime(2020,9, 29, 22, 20)
    print(dt.strftime('%Y-%m-%d-%H-%M'))

# lambda 트리거 될 때 dt 오브젝트를 event 요소로 넘겨주면 괜찮을 것 같다. (현재 invoke 된 시간.)