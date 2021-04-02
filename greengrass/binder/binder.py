from libs.util import get_lambda_input_message
from time import sleep


def handler(event, context):
    while True:
        sleep(1)
        print(get_lambda_input_message(event))
