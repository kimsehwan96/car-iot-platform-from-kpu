import os

PUBLISH_TOPIC = os.environ.get('PUBLISH_TOPIC')

def get_publish_topic():
    return PUBLISH_TOPIC

    