import os
import requests

IPC_TOPIC = os.environ.get('IPC_TOPIC', 'ipc')
CLOUD_TOPIC = os.environ.get('CLOUD_TOPIC', 'data')


def get_ipc_topic():
    return IPC_TOPIC


def get_cloud_topic():
    return CLOUD_TOPIC

def get_fields():
    pass


def get_lambda_input_message(event):
    """
    IPC용으로 사용하는 mqtt 메시지를 파싱하기 위한 함수. 테스트 예정
    """
    try:
        message = event
    except Exception as e:
        print("error occured", e)
    return message


def check_connected_to_internet(url='https://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

