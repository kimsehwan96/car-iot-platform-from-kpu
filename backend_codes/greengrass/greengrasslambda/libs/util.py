import os
import time
import datetime

PUBLISH_TOPIC = os.environ.get('PUBLISH_TOPIC')

def get_publish_topic():
    return PUBLISH_TOPIC

def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

