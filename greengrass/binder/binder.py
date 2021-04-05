import json
from libs.util import get_lambda_input_message
from time import sleep
from _thread import start_new_thread
from dispatcher.test_dispacter import TestDispatcher, TestDispatcher2, TestDispatcher3


dispatchers = [TestDispatcher(), TestDispatcher2(), TestDispatcher3()]


class BinderManager:
    def __init__(self):
        self.buffer = None

    def bind(self, message):
        print('original message : ', message)
        data = message.get('payload')
        if not data:
            print('no data..')
        self.buffer = data
        print(f'success to parse : {self.buffer}')

    def consume(self):
        # 여기서 디스패쳐 각 스레드를 실행시키면 될 듯. 공유 자원은 락 걸어놓자.
        if self.buffer:
            print("data consume.. ")
            for dispatcher in dispatchers:
                dispatcher.run(json.dumps(self.buffer))
            self.buffer = None
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
