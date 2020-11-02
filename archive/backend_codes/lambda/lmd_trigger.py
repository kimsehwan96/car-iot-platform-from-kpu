# TODO: 람다를 1시간마다 invoke 하기 위한 코드
# events -> cron 스케줄 이용.
# 예를들어 16시에 인보크 되어 트리거를 날리면, 15 ~ 16시 사이의 데이터를 처리해야 하는거니까
# 애초에 datetime 오브젝트를 15시걸 주고, 15시 00분부터 59분까지를 취합하도록 하면 될거같네.
# 중간중간 비는건 모두 예외처리하고, 비지 않는것만 처리하기 (s3 rawdata)

import boto3
import abc
import os
import datetime
import time
import json

BUCKET_NAME = os.environ.get('RAW_BUCKET', 'if this texts show, Env var wasnt detectd')
TRIGGERD_LAMDA = os.environ.get('TRIGGERD_LAMDA', 'batch-lambda-dev-stat-get-trigger')
os.environ['TZ'] = 'Asia/Seoul'

lmd = boto3.client('lambda')

def timenow_dt_strftime():
    time_now = time.time()
    dt = datetime.datetime.fromtimestamp(time_now)
    return dt.strftime('%Y-%m-%d-%H-%M')
    #invoke 요청 할 당시의 datetime object
    
def handler(event, context):
    print("this lambda has invoked!! (cron test lambda)")
    print("this is BUCKET_NAME {}".format(BUCKET_NAME))

    #dt = timenow_dt()
    #dt = datetime.datetime(2020,9, 29, 22, 20)
    print(timenow_dt_strftime())

    try:
        lmd.invoke(
            FunctionName=TRIGGERD_LAMDA,
            InvocationType='Event', Payload=json.dumps({'dt' : timenow_dt_strftime()}))
    except  Exception as e:
        print("Error occured when triggering another lambda! {}".format(e))

# lambda 트리거 될 때 dt 오브젝트를 event 요소로 넘겨주면 괜찮을 것 같다. (현재 invoke 된 시간.)