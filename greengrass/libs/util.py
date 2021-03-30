import os

IPC_TOPIC = os.environ.get('IPC_TOPC', 'ipc')
CLOUD_TOPIC = os.environ.get('CLOUD_TOPIC', 'kpu/iot')


def get_ipc_topic():
    return IPC_TOPIC


def get_cloud_topic():
    return CLOUD_TOPIC


def get_lambda_input_message(event):
    try:
        message = event
    except Exception as e:
        print("error occured", e)
    return message
