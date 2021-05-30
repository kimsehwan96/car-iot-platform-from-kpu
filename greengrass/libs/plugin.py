from _thread import start_new_thread
from typing import Callable


def run_plugin_thread(func, option={}) -> None:
    try:
        start_new_thread(func, (option,))
    except Exception as e:
        print("error : ", e)
