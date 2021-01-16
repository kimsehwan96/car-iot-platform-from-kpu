from _thread import start_new_thread
from enum import Enum

class PluginType(Enum):
    TEST_SOCKET = 1
    CAN = 2

def run_plugin_thread(hanlder_func, data_source: dict = {}, option: dict = {}) -> None:
    try:
        start_new_thread(hanlder_func, (data_source, option))
    except Exception as e:
        print("Error ouccured when start plugin thread :", e)

# 데이터 수집을 위한 스레드 호출 부