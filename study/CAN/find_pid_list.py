"""
find avaliable pids.

"""

import can
from time import sleep

PID_REQUEST = 0x7DF
PID_REPLY = 0x7E8

SHOW_CURRENT_DATA = 0x01
SHOW_FREEZE_FRAME_DATA = 0x02
SHOW_TROUBLE_CODES = 0x03


def is_valid_reply(message) -> bool:
    if message.arbitration_id != PID_REPLY:
        return False
    else:
        return True

pid_check_list = [0x00, 0x20, 0x40, 0x80, 0xa0, 0xc0]

find_pid_msg = [0x02,
                SHOW_CURRENT_DATA,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00
                ]

msgs = [[0x02, SHOW_CURRENT_DATA, x, 0x00, 0x00, 0x00, 0x00, 0x00] for x  in pid_check_list]
cms = []
for m in msgs:
    cms.append(can.can.Message(arbitration_id=PID_REQUEST, data=m, extended_id=False))



channel = 'can0'
bus_type = 'socketcan_native'
bus = can.interface.Bus(channel=channel, bustype=bus_type)

# msg = can.Message(arbitration_id=PID_REQUEST, data=find_pid_msg, extended_id=False)

# bus.send(msg)

# sleep(0.1)

for cm in cms:
    bus.send(cm)
    sleep(0.1)
    while True:
        recv = bus.recv()
        if is_valid_reply(recv):
            print(recv)
            break
        else:
            continue

# while True:
#     for cm in cms:
#         recv = bus.recv()
#         if is_valid_reply(recv):
#             print(recv)
#         break
#     else:
#         continue

print('done !')

"""
A request for this PID returns 4 bytes of data (Big-endian). 
Each bit, from MSB to LSB, represents one of the next 
32 PIDs and specifies whether that PID is supported.

응답 받은 데이터를 bin으로 변경.
00으로 질의하면 0x00 ~ 0x20에 해당하는 내용
즉 32개 
>>> a = 0xBE 1F A8 13
>>> a
3189745683
>>> bin(a)
'0b10111110000111111010100000010011'
>>> 

00

b6 3f a8 13    Channel: can0
80 1f f0 11     Channel: can0
fe d0 84 01     Channel: can0


"""

a = 0xb63fa813
b = 0x801ff011
c = 0xfed08401

print(bin(a))
print(bin(b))
print(bin(c))

a = '10110110001111111010100000010011'
b = '10000000000111111111000000010001'
c = '11111110110100001000010000000001'


one = [hex(x) for x in range(1, 33)]
two = [hex(x) for x in range(33, 65)]
three = [hex(x) for x in range(65, 97)]

for i, v in enumerate(one):
    if a[i] == '1':
        print(v)

for i, v in enumerate(two):
    if b[i] == '1':
        print(v)

for i, v in enumerate(three):
    if c[i] == '1':
        print(v)

