import unittest
from . import create_dispatchers
from .base_dispatcher import BaseDispatcher


# TODO : move all of custom exeption with exception.py  in libs.

class NotSupportedDispatcher(Exception):
    def __init__(self):
        super().__init__('지원하지 않는 Dispatcher 타입임')


class DispatcherTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def testCreateDispatcher(self):
        config = ['test2']
        self.assertRaises(NotSupportedDispatcher, create_dispatchers(config))
        config = ['test', 'websocket', 'mqtt']
        dispatchers = create_dispatchers(config)
        for dispatcher in dispatchers:
            self.assertIsInstance(dispatcher, BaseDispatcher)


if __name__ == '__main__':
    unittest.main()
