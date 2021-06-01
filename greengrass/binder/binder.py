import json
from libs.util import get_lambda_input_message
from time import sleep
from _thread import start_new_thread
from dispatcher.test_dispatcher import TestDispatcher
from dispatcher.mqtt_dispatcher import MqttDispatcher
from dispatcher.websocket_dispatcher import WebSocketDispatcher
from dispatcher.influx_dispatcher import InfluxDispatcher
from dispatcher.storage_dispatcher import StorageDispatcher

dispatchers = [
    TestDispatcher(),
    MqttDispatcher(),
    WebSocketDispatcher(),
    StorageDispatcher(),
    # InfluxDispatcher()
]


class BinderManager:
    def __init__(self) -> None:
        self.buffer = None

    def bind(self, message) -> None:
        data = message.get('payload')
        if not data:
            print('no data..')
        self.buffer = data

    def consume(self) -> None:
        # 여기서 디스패쳐 각 스레드를 실행시키면 될 듯. 공유 자원은 락 걸어놓자.
        if self.buffer:
            for dispatcher in dispatchers:
                dispatcher.run(json.dumps(self.buffer))
            self.buffer = None
        else:
            print("no data..")


bm = BinderManager()


def bind(message) -> None:
    bm.bind(message)


def handler(event, context) -> None:
    print("binder handler is working,,")
    message = get_lambda_input_message(event)
    bind(message)


def consumer() -> None:
    while True:
        sleep(1)
        print('consumer is running')
        try:
            bm.consume()
        except Exception as e:
            print(e)


start_new_thread(consumer, ())
