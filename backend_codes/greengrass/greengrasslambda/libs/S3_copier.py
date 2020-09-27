import boto3
import os
import csv

# TODO: S3 에 1분간 저장된 원본 데이터를 저장하는 로직이 들어 갈 예정
DEVICE_ID = os.environ.get("AWS_IOT_THING_NAME", 'test_id')
s3 = boto3.resource('s3')

