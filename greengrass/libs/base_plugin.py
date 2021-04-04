from abc import ABCMeta, abstractmethod
from .util import get_ipc_topic
from .ipc_helper import IpcHelper
from typing import List
from time import sleep


class BasePlugin(metaclass=ABCMeta):
    def __init__(self, option={}):
        self.topic = get_ipc_topic()
        self._option = option
        self._ipc_helper = IpcHelper(self.topic, option=option)
        self._buffer = []

    @property
    def data(self) -> List[int or float]:
        return self._buffer

    @data.setter
    def data(self, data):
        self._buffer = data

    # p.data = value

    @abstractmethod
    def collect_data(self):
        pass

    def entry(self):
        self._ipc_helper.scheduler_start()
        while True:
            self.collect_data()
            self._ipc.push_data(self.data)
            sleep(1)
