from __future__ import print_function

import time
import threading

import can

# serial 케이블을 이용한 캔 통신.

def send_cyclic(bus, msg, stop_event):
    print("Start to send a message every 1s")
    start_time = time.time()
    while not stop_event.is_set():
        msg.timestamp = time.time() - start_time
        bus.send(msg)
        print("tx: {}".format(tx_msg))
        time.sleep(1)
    print("Stopped sending messages")


def receive(bus, stop_event):
    print("Start receiving messages")
    while not stop_event.is_set():
        rx_msg = bus.recv(1)
        if rx_msg is not None:
            print("rx: {}".format(rx_msg))
    print("Stopped receiving messages")

if __name__ == "__main__":
    server = can.interface.Bus(bustype='serial', channel='/dev/ttyS10') # device 파일이 /dev/ttyS10 과 같은 시리얼 디바이스 파일 -> 라즈베리 파이에서 찾아야 함
    client = can.interface.Bus(bustype='serial', channel='/dev/ttyS11')

    tx_msg = can.Message(arbitration_id=0x01, data=[0x11, 0x22, 0x33, 0x44,
                                                    0x55, 0x66, 0x77, 0x88])

    # Thread for sending and receiving messages
    stop_event = threading.Event()
    t_send_cyclic = threading.Thread(target=send_cyclic, args=(server, tx_msg,
                                                               stop_event))
    t_receive = threading.Thread(target=receive, args=(client, stop_event))
    t_receive.start()
    t_send_cyclic.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    stop_event.set()
    server.shutdown()
    client.shutdown()
    print("Stopped script")

    
    # TODO: 캔 통신을 통해 데이터를 수집하고 / mqtt Publisher 로 전달해줄 Class 설계 필요.
    # 차량마다 다른 메모리 번지수 대응을 위해, data[16진수] 부분을 profile 화 할 필요 있음.
    