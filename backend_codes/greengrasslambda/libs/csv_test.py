import csv
import datetime
import time
from .util import *




fields = ['rpm', 'speed', 'brake']
data = [[1, 2, 3], [1,2,3], [1,2,3], [1,2,3]]

if __name__ == "__main__":
    with open ('test_1.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)

# 데이터 구조
# timestamp 필드1번 필드2번 필드3번
# 시간        데이터   데이터  데이터

# fields = ['timestamp', 필드들]
# data = [  [시간, 필드들] , [시간, 필드들] ] 
# 이렇게 전달 되어야 한다. hi