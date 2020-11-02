import os

def get_publish_topic():
    return os.environ.get('PUBLISH_TOPIC')

def get_raw_data_bucket():
    return os.environ.get('RAW_DATA_BUCKET_NAME')

def get_group_id():
    return os.environ.get('GROUP_ID')


'''
environ var's are defined in provisioning/deployments/function.defaults.conf
'''

