import os
import sys
import logging

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
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('buffered_data', namespace='/binder')
def uiapp_broadcast(data):
    print(' -  - - - - - - - -- - - this is socketio data ', data)
    emit('rtdata', data, broadcast=True)


def handler(event, context):
    pass


socketio.run(app, host='0.0.0.0', port=5000, debug=True)
print('Success to run')
