from time import sleep
from random import random, randint
from libs import util
from libs.plugin import run_plugin_thread
from libs.ipc_helper import IpcHelper

TOPIC = util.get_ipc_topic()


def handler(event, context):
    pass


def test_plugin(option={}):
    ipc = IpcHelper(TOPIC, option=option)
    ipc.scheduler_start()
    while True:
        ipc.push_data([randint(0, 100) for x in range(5)])
        print('data was published')
        sleep(1)


def run():
    run_plugin_thread(test_plugin)


if __name__ == '__main__':
    pass
else:
    run()
