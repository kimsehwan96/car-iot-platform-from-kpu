from libs.util import get_lambda_input_message
from time import sleep
from _thread import start_new_thread


class BinderManager:
    def __init__(self):
        self.buffer = []

    def bind(self, message):
        data = message.get('payloads')
        if not data:
            print('no data..')
        self.buffer = data
        print(f'success to parse : {self.buffer}')

    def consume(self):
        if self.buffer:
            print("data consume.. ")
            self.buffer = []
        else:
            print("no data..")


bm = BinderManager()


def bind(message):
    bm.bind(message)


def handler(event, context):
    print("binder handler is working,,")
    message = get_lambda_input_message(event)
    bind(message)


def consumer():
    while True:
        sleep(1)
        print('consumer is running')
        try:
            bm.consume()
        except Exception as e:
            print(e)


start_new_thread(consumer, ())
