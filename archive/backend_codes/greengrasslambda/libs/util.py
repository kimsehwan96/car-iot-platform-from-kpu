import os
import time
import datetime

PUBLISH_TOPIC = os.environ.get('PUBLISH_TOPIC')

def get_publish_topic():
    return PUBLISH_TOPIC

def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

def get_year(dt):
    return dt.year

def get_month(dt):
    return dt.month

def get_day(dt):
    return dt.day

def get_hour(dt):
    return dt.hour

def get_min(dt):
    return dt.minute

def get_second(dt):
    return dt.second
    

