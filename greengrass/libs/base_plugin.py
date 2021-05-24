from abc import ABCMeta, abstractmethod
from .util import get_ipc_topic
from .ipc_helper import IpcHelper
from .meta_singleton import Singleton
from typing import List
from time import sleep

# TODO : fix option's structure.


class BasePlugin(metaclass=ABCMeta):
    def __init__(self, fields: [str], option=None):
        if option is None:
            option = {}
        self.topic = get_ipc_topic()
        self._option = option
        self._ipc_helper = IpcHelper(self.topic, fields, option=option)
        self._buffer = []

    @property
    def data(self) -> List[int or float]:
        return self._buffer

    @data.setter
    def data(self, data) -> None:
        self._buffer = data

    @abstractmethod
    def collect_data(self):
        """
        실제 디바이스로부터 데이터를 받는 로직이 들어가야 함.

        self.data = 얻어온 데이터

        이렇게 구현이 되어야 함.

        얻어온 데이터는 list 혹은 deque. 아직 미정
        """
        raise NotImplementedError("추상 메서드입니다.")

    def entry(self, option={}):
        """
        스레드가 실행될 엔트리 메서드.
        """
        self._option = option
        self._ipc_helper.scheduler_start()
        while True:
            self.collect_data()
            self._ipc_helper.push_data(self.data)
            sleep(1)
