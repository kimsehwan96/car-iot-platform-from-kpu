import os
import sys
import logging
import json

from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask_cors import CORS
from _thread import start_new_thread

logging.basicConfig(level=logging.INFO)

async_mode = None
app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins='*')
thread = None
thread_lock = Lock()


@app.route('/')
def index() -> None:
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/oilPrice')
def oil_proce() -> None:
    """
    오늘 전국 주유소 평균 유가정보를 제공하는 API
    프론트 코드 및 내부적으로 소비할 API임
    """
    return json.dumps({
        'price': 1500
    })


@socketio.on('buffered_data', namespace='/binder')
def uiapp_broadcast(data) -> None:
    """
    실시간 데이터를 송신하는 부분.
    buffered_data 라는 이벤트 수신시 localhost/binder 로 실시간 데이터를 보냄.
    buffered_data이벤트 및 data는 파이썬 코드 내에서 (websocket_dispatcher)에서 보낸다.
    """
    print(' -  - - - - - - - -- - - this is socketio data ', data)
    emit('rtdata', data, broadcast=True)


def handler(event, context) -> None:
    pass


socketio.run(app, host='0.0.0.0', port=5000, debug=True)
print('Success to run')
