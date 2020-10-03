import os
import datetime
import time
import boto3


def handler(event, context):
    print("this lambda has been invoked !")
    print(event)

    if event.get('dt'):
        dt = event.get('dt')
    else:
        print("No dt got")

    print(dt) # '2020-09-29-22-20' 년/월/일/시간/분 -> 22시 20분
    # 22시 0분부터 59분까지 데이터를 다운로드 받아서 필드값은 맨 위 한번만 정의하고,
    # 그 밑으로 데이터들을 쭉 append 하고, 최소, 최대, 평균값 만들어 DB 에 저장하기.