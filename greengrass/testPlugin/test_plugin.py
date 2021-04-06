from random import randint
from libs.plugin import run_plugin_thread
from libs.base_plugin import BasePlugin


def handler(event, context):
    pass


class TestPlugin(BasePlugin):
    def collect_data(self):
        self.data = [randint(0, 100) for x in range(16)]
        print('this is bufferd data: ', self.data)


tp = TestPlugin()


def run():
    run_plugin_thread(tp.entry)


if __name__ == '__main__':
    pass
else:
    run()
