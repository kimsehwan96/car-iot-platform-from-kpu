import json
import time
import threading
import greengrasssdk


class IpcHelper:
    """
    IPC는 mqtt를 이용해서 우선 진행 해볼 예정.
    가능하다면 unix domain socket?
    """

    def __init__(self, ipc_topic: str, fields: [str], option: {}) -> None:
        self.ipc_topic = ipc_topic
        self._channel = greengrasssdk.client('iot-data')
        self._buffer = []
        self._fields = fields
        self._message = {}

    def get_topic(self) -> str:
        return self.ipc_topic

    def push_data(self, data) -> None:
        self._buffer = data

    def _make_message(self) -> dict:
        return {
            'payload': {
                'fields' : self._fields,
                'values' : self._buffer,
                'timestamp': time.time()
            }
        }

    def scheduler(self) -> None:
        print('this is buf  ,', self._buffer)
        buf_len = len(self._buffer)
        if buf_len == 0:
            print('no buf')
            return

        message = self._make_message()

        self._channel.publish(
            topic=self.ipc_topic,
            payload=json.dumps(message)
        )

        print(f'message publish done by topic : ,{self.ipc_topic}, message : {message}')

    def scheduler_start(self) -> None:
        def wrapper():
            while True:
                self.scheduler()
                time.sleep(1)

        threading.Thread(target=wrapper).start()
