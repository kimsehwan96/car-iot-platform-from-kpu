import boto3
import os

S3_SAVE_BUCKET = os.environ.get('S3_SAVE_BUCKET', 'sehwan-an2-edge-dev-rawdata')
PATH = os.getcwd()
s3 = boto3.resource('s3')





if __name__ == "__main__":
    s3.meta.client.upload_file(
        PATH + '/rawdata_2020_9_28_19_5.csv', 
        S3_SAVE_BUCKET, 
        'tmp/test.csv')
    # 사용법. s3.meta.client.upload_file(실제 파일 경로, 버킷 네임, 어떤 경로로 저장할건지.)
