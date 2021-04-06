import os

IPC_TOPIC = os.environ.get('IPC_TOPC', 'ipc')
CLOUD_TOPIC = os.environ.get('CLOUD_TOPIC', 'data')


def get_ipc_topic():
    return IPC_TOPIC


def get_cloud_topic():
    return CLOUD_TOPIC


def get_lambda_input_message(event):
    """
    IPC용으로 사용하는 mqtt 메시지를 파싱하기 위한 함수. 테스트 예정
    """
    try:
        message = event
    except Exception as e:
        print("error occured", e)
    return message
