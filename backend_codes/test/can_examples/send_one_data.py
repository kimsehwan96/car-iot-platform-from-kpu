#!/usr/bin/env python3

import can
from time import sleep

conf = {
    'bustype' : 'socketcan',
    'channel' : 'vcan0',
    'receive_own_messages' : True
}

def send_one():
    with can.interface.Bus(**conf) as bus:
        msg = can.Message(
            arbitration_id=0xC0FFEE,
            data=[0, 25, 0, 1, 3, 1, 4, 1],
            is_extended_id=True
        )

    try:
        bus.send(msg)
        print("message sent on {}".format(bus.channel_info))
    except can.CanError as e:
        print("error occured {}".format(e))

if __name__ == "__main__":
    while True:
        sleep(1)
        send_one()

        