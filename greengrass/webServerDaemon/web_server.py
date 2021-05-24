import sys

from http.server import (
    ThreadingHTTPServer,
    SimpleHTTPRequestHandler
)
from threading import Thread


def run(dirname, port):
    server_addr = ("", port)

    class Handler(SimpleHTTPRequestHandler):

        def __init__(self, *args, **kwargs) -> None:
            super(Handler, self).__init__(*args, directory=dirname, **kwargs)

        def send_error(self, code, message=None) -> None:
            pass

    with ThreadingHTTPServer(server_addr, Handler) as httpd:
        sa = httpd.socket.getsockname()
        serve_message = f'Start http server on {sa[0]}:{sa[1]} for {dirname} dir'
        print(serve_message)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)


def handler(event, context) -> None:
    pass


dirname = 'app'
port = 8888
Thread(target=run, args=(dirname, port)).start()

if __name__ == '__main__':
    dirname = 'app'
    port = 8888
    Thread(target=run, args=(dirname, port)).start()
