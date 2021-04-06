import socketio
from .base_dispatcher import BaseDispatcher
from time import sleep

socketio = socketio.Client()


class WebSocketDispatcher(BaseDispatcher):
    def __init__(self):
        self.is_init = False
        self.threshold = 5
        self.timeout = 5

    # TODO: connect 메서드를 리팩터링하기.
    def connect(self):
        if self.is_init:
            return
        try:
            socketio.connect('http://0.0.0.0:5000', namespaces='/binder')
            self.is_init = True
        except Exception as e:
            print('failed to connect websocket ', e)
            for cnt in range(self.threshold):
                try:
                    print('retry to connect websocket : ', cnt + 1)
                    socketio.connect('http://0.0.0.0:5000', namespaces='/binder')
                    return
                except Exception as e:
                    print('failed to reconnect')
                    sleep(self.timeout)

                self.is_init = False

    def emit(self, data):
        if not self.is_init:
            self.connect()
        try:
            socketio.emit('buffered_data', data, namespace='/binder')
            print(f'---------- emit socketio data -------- {data}')
        except Exception as e:
            print('socketio emit error ', e)

    def relay(self, data: str):
        self.emit(data)
