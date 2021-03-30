from _thread import start_new_thread


def run_plugin_thread(func, option={}):
    try:
        start_new_thread(func, (option,))
    except Exception as e:
        print("error : ", e)
