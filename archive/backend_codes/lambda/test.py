# TODO: 통계 데이터를 만들기 위한 람다.
# 1. 테스트 할 것, S3 에 {Greengrass Group Name}/rawdata_2020-09-29-22-01.csv 와 같이 각 Group Name 별로 저장되어있다.
# 첫번째 테스트. S3 에서 특정 시간 CSV 파일만 모두 다운로드 받아보기 (중간에 빈 데이터 예외 처리 하기.)
import boto3
import os
import pandas as pd
import datetime
import json
from decimal import Decimal

AWS_THING_NAME = os.environ.get('AWS_THING_NAME', 'test-group_Core')
BUCKET_NAME = 'sehwan-an2-edge-dev-rawdata'
HOUR_STAT_TABLE = os.environ.get('HOUR_STAT_TABLE', 'dynamodb-resources-Hour-stat')
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(HOUR_STAT_TABLE)

def make_stream_obj_to_ary(raw_data): #raw_data <- s3.get_ojbject(**kwargs).get('Body').read()
    data = raw_data.decode()
    ary = []
    ary = data.split('\r\n')
    if ary[-1] == '':
        ary.pop() #마지막 '' 요소 삭제.
    else:
        pass
    return ary

def concat_dataFrame(raw_ary, fields):  # 분마다 데이터프레임으로 만들어서 합침
    df_ary = []
    for idx in range(len(raw_ary)):
        tmp_ary = [x.split(',') for x in raw_ary[idx]]
        df_ary.append(pd.DataFrame(tmp_ary[1:]))
        df_ary[idx].columns=fields
    result = pd.concat(df_ary)
    return result

def cal_avg(result, fields):   # 평균 계산 
    col = fields[1:]
    avg_pd = result.mean(axis = 0)
    avg_dict = {}
    for v in col:
        avg_dict[v] = avg_pd[v]
    return list(map(int , list(avg_dict.values()))) #각 원소가 int인 리스트 형태로 리턴하기 위함..

def cal_max(result, fields):   # 최대값 계산 
    col = fields[1:]
    max_pd = result.max(axis = 0)
    max_dict = {}
    for v in col:
       max_dict[v] = max_pd[v]
    return list(map(int , list(max_dict.values()))) #각 원소가 int인 리스트 형태로 리턴하기 위함..

def cal_min(result, fields):   # 최소값 계산 
    col = fields[1:]
    min_pd = result.min(axis = 0)
    min_dict = {}
    for v in col:
       min_dict[v] = min_pd[v]
    return list(map(int , list(min_dict.values()))) #각 원소가 int인 리스트 형태로 리턴하기 위함..

def cal_std(result, fields):   # 표준편차 계산 
    col = fields[1:]
    std_pd = result.std(axis = 0)
    std_dict = {}
    for v in col:
       std_dict[v] = std_pd[v]
    return list(map(int , list(std_dict.values()))) #각 원소가 int인 리스트 형태로 리턴하기 위함..

def cal_datetime():
    return datetime.datetime(2020,9, 29, 21) #tempary..


def save_to_dynamodb(fields, avg, min, max, std):
    data = {
        'deviceId' : AWS_THING_NAME,
        'timestamp' : cal_datetime().strftime('%Y-%m-%d-%H'),
        'fields' : fields,
        'avg' : avg,
        'min' : min,
        'max' : max,
        'std' : std
    }
    return table.put_item(
        Item = data
    )
    #print(payload)

if __name__=="__main__":
    S3_KEYS = [
        'test-group_Core/rawdata_2020-09-29-22-20.csv',
        'test-group_Core/rawdata_2020-09-29-22-21.csv',
        'test-group_Core/rawdata_2020-09-29-22-23.csv',
        'test-group_Core/rawdata_2020-09-29-22-24.csv'
    ] # 향후 트리거된 람다로부터 이 키들을 생성 할 예정임.
    raw_ary = []
    for v in S3_KEYS:
        try:
            obj = s3.get_object(
                Bucket = BUCKET_NAME,
                #Key = '{}/rawdata_2020-09-29-22-20.csv'.format(AWS_THINS_NAME)
                Key = v
            )
        except s3.exceptions.NoSuchKey as e:
            print("error occured , No such Key") #key 없을 때 예외 처리 로직.
        try:
            raw_data = obj.get('Body').read()
            raw_ary.append(make_stream_obj_to_ary(raw_data))
        except Exception as e:
            print("error occured {}".format(e))

    if not(raw_ary): # 만약 어레이에 어떤 데이터도 들어오지 않았다면 람다 종료.
        print("there is no data for processing")
        exit(0)
    else:
        pass

    fields = raw_ary[0][0].split(',')
    
    result = concat_dataFrame(raw_ary, fields)   #데이터프레임으로 합치기
        
    for v in fields[1:]: # 타임스탬프를 제외한 필드를 숫자 데이터로 변환함.
        result[v]= pd.to_numeric(result[v])

    avg_result = cal_avg(result, fields)
    max_result = cal_max(result, fields)
    min_result = cal_min(result, fields)
    std_result = cal_std(result, fields)

    print(avg_result, max_result, min_result, std_result)
    res = save_to_dynamodb(fields[1:], avg_result, max_result, min_result, std_result)
    print(res)