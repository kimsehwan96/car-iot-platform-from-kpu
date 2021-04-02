from libs.util import get_lambda_input_message
from time import sleep
from _thread import start_new_thread

MSG = None


def handler(event, context):
    print("binder hanlder is working,,")
    message = get_lambda_input_message(event)
    wrapper(message)


def show_data(message):
    print(message)
    print('show data processed.')


def wrapper(message):
    start_new_thread(show_data, (message,))
