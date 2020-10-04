# TODO: 통계 데이터를 만들기 위한 람다.
# 1. 테스트 할 것, S3 에 {Greengrass Group Name}/rawdata_2020-09-29-22-01.csv 와 같이 각 Group Name 별로 저장되어있다.
# 첫번째 테스트. S3 에서 특정 시간 CSV 파일만 모두 다운로드 받아보기 (중간에 빈 데이터 예외 처리 하기.)
import boto3
import os
import pandas as pd

AWS_THINS_NAME = os.environ.get('AWS_THING_NAME', 'test-group_Core')
BUCKET_NAME = 'sehwan-an2-edge-dev-rawdata'
s3 = boto3.client('s3')

def make_stream_obj_to_ary(raw_data): #raw_data <- s3.get_ojbject(**kwargs).get('Body').read()
    data = raw_data.decode()
    ary = []
    ary = data.split('\r\n')
    if ary[-1] == '':
        ary.pop() #마지막 '' 요소 삭제.
    else:
        pass
    #print(ary)
    return ary

def concat_dataFrame(raw_ary, fields):  # 분마다 데이터프레임으로 만들어서 합침
    df_ary = []
    for idx in range(len(raw_ary)):
        tmp_ary = [x.split(',') for x in raw_ary[idx]]
        df_ary.append(pd.DataFrame(
         tmp_ary[1:]
            )
        )
        df_ary[idx].columns=fields
    result = pd.concat(df_ary)
    return result

def cal_avg(result, fields):   # 평균 계산 
    col = fields[1:]
    avg_pd = result.mean(axis = 0)
    avg_dict = {}
    for v in col:
        avg_dict[v] = avg_pd[v]
    return avg_dict

def cal_max(result, fields):   # 최대값 계산 
    col = fields[1:]
    max_pd = result.max(axis = 0)
    max_dict = {}
    for v in col:
       max_dict[v] = max_pd[v]
    return max_dict

def cal_min(result, fields):   # 최소값 계산 
    col = fields[1:]
    min_pd = result.min(axis = 0)
    min_dict = {}
    for v in col:
       min_dict[v] = min_pd[v]
    return min_dict

def cal_std(result, fields):   # 표준편차 계산 
    col = fields[1:]
    std_pd = result.std(axis = 0)
    std_dict = {}
    for v in col:
       std_dict[v] = std_pd[v]
    return std_dict


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

    #print(raw_ary) # 이거 가지고 pandas 이용 처리를 해볼거임
    fields = raw_ary[0][0].split(',')
    #print(fields)
    
    result = concat_dataFrame(raw_ary, fields)   #데이터프레임으로 합치기
        
    for v in fields[1:]: # 타임스탬프를 제외한 필드를 숫자 데이터로 변환함.
        result[v]= pd.to_numeric(result[v])
    #print(result.describe())
    
    avg_result = cal_avg(result, fields)
    max_result = cal_max(result, fields)
    min_result = cal_min(result, fields)
    std_result = cal_std(result, fields)

    print(avg_result, max_result, min_result, std_result)

    #s3.exceptions.NoSuchKey

# lambda가 임의로 invoke 되었을 때 dt 받아서 출력해보기.


    #print(obj)
    #body = obj.get('Body')
    #print(dir(body))
    #raw_data = body.read()
    #print(raw_data)
    #print(raw_data.decode('utf-8')) # can detect with csv file?
    #print(type(raw_data.decode('utf-8')))

    #make_stream_obj_to_ary(raw_data) # 마지막에 ''가 들어오네





# body.read()
'''

b'timestamp,rpm,speed,brake,oilTemp,oilStatus\r\n1601385541.0451908,193,155,35,174,49\r\n1601385542.0400403,191,93,60,186,160\r\n1601385543.041043,3,46,163,39,200\r\n1601385544.0414963,8,174,103,160,141\r\n1601385545.0712392,171,158,155,46,59\r\n1601385546.08011,148,18,63,66,152\r\n1601385547.0808315,37,70,80,2,69\r\n1601385548.0823941,103,35,171,62,110\r\n1601385549.1141858,83,173,156,104,77\r\n1601385550.114582,144,88,128,35,82\r\n1601385551.1169212,87,124,149,120,143\r\n1601385552.1286738,129,104,79,88,147\r\n1601385553.160199,87,46,3,169,126\r\n1601385554.1606529,75,147,10,42,20\r\n1601385555.1628735,129,168,196,107,184\r\n1601385556.1640532,29,151,92,87,102\r\n1601385557.1710994,84,132,176,136,154\r\n1601385558.1722326,121,152,109,116,98\r\n1601385559.1725821,161,125,73,135,142\r\n1601385560.1747282,124,116,183,116,139\r\n1601385561.1818147,200,11,132,110,94\r\n1601385562.2096698,127,94,109,142,163\r\n1601385563.2146564,92,111,117,59,191\r\n1601385564.2157128,187,162,90,58,156\r\n1601385565.2305045,92,168,119,47,68\r\n1601385566.2666454,163,200,175,138,66\r\n1601385567.275738,107,68,79,130,13\r\n1601385568.2766292,13,85,61,55,184\r\n1601385569.2777157,128,8,75,184,181\r\n1601385570.2809072,47,31,182,42,132\r\n1601385571.2821338,58,57,164,103,194\r\n1601385572.2867599,196,4,82,60,7\r\n1601385573.2896464,160,63,90,36,168\r\n1601385574.3093371,51,113,153,12,174\r\n1601385575.3126507,10,171,95,86,125\r\n1601385576.313722,85,1,101,70,43\r\n1601385577.3159134,109,195,127,90,191\r\n1601385578.3180013,35,18,65,17,93\r\n1601385579.328271,90,134,81,139,177\r\n1601385580.329004,65,195,197,112,178\r\n1601385581.330496,191,191,85,59,72\r\n1601385582.3323638,26,35,76,166,127\r\n1601385583.3752112,99,27,144,144,99\r\n1601385584.3754988,110,21,85,184,169\r\n1601385585.3911355,52,100,83,190,116\r\n1601385586.3919082,180,7,16,169,155\r\n1601385587.3921463,64,12,131,130,131\r\n1601385588.3997073,180,127,127,96,9\r\n1601385589.4006138,172,41,142,33,64\r\n1601385590.4017577,62,84,52,46,96\r\n1601385591.405762,45,169,66,122,70\r\n1601385592.4070077,72,30,76,179,184\r\n1601385593.408085,190,85,47,42,9\r\n1601385594.4084573,99,196,197,90,63\r\n1601385595.4112647,115,133,105,192,138\r\n1601385596.4129593,64,76,197,182,149\r\n1601385597.424719,32,96,163,97,193\r\n1601385598.4259129,162,93,78,115,179\r\n1601385599.4359295,94,168,78,167,196\r\n'

'''

''' 
raw_data.decode('utf-8')
timestamp,rpm,speed,brake,oilTemp,oilStatus
1601385541.0451908,193,155,35,174,49
1601385542.0400403,191,93,60,186,160
1601385543.041043,3,46,163,39,200
1601385544.0414963,8,174,103,160,141
'''

# 위 데이터는 str 형태지만, 개행문자를 기준으로 행을 하나씩 분리가 가능 할 것.