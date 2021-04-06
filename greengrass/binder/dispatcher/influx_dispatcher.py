from .base_dispatcher import BaseDispatcher


class InfluxDispatcher(BaseDispatcher):
    def __init__(self):
        pass

    def relay(self, data: str):
        print('mqtt dispatcher got relayed data {}'.format(data))

    # TODO : We specify below things. Caution : We should not make dependencies.
    # 1. Influxdb url
    # 2. Influxdb table name
    # 3. Influxdb organzation, token, etc...

