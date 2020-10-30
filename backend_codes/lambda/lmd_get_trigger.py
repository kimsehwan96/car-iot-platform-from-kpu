import os
import datetime
import time
import boto3

os.environ['TZ'] = 'Asia/Seoul'

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
    # 결정 할 거. 트리거 할 때 1시간을 뺄지, 여기서 1시간을 뺄지 (with timedelta)
    convert_dt = datetime.datetime.strptime(dt, ('%Y-%m-%d-%H-%M'))
    print(convert_dt)

    ary = make_s3_key_ary(convert_dt)
    print(ary)

def make_s3_key_ary(datetime_object):
    ary = []
    dt_year = datetime_object.year
    dt_month = datetime_object.month
    dt_day = datetime_object.day
    dt_hour = datetime_object.hour
    dt_minute = datetime_object.minute
    # 2020-09-29-22-00 ~ 2020-09-29-59 의 string array를 만들기
    time_format = '{}-{}-{}-{}'.format(
        dt_year,
        dt_month,
        dt_day,
        dt_hour
    )
    ary = [ 'rawdata_' + time_format + '-' + str(x).zfill(2) for x in range(60)]
    #str(object).zfill(number) -> number 만큼 문자열 앞에 0을 채워줌
    return ary

if __name__ == "__main__":
    dt = datetime.datetime.now()
    ary = make_s3_key_ary(dt)
    print(ary)
