import threading
import unittest
import socket
from client import read_url_file, send_urls, send_url


def run_fake_server():
    HOST = '127.0.0.1'
    PORT = 3000
    server_sock = socket.socket()
    server_sock.bind((HOST, PORT))
    server_sock.listen(0)
    server_sock.accept()
    server_sock.sendall(b"{'result': 200}")
    server_sock.close()


class TestClient(unittest.TestCase):

    def test_read_url_file(self) -> None:
        self.assertTrue(read_url_file('./test_files/test_urls.txt'), ['https://en.wikipedia.org/wiki/1700', 'q'])

    def test_send_url_connect_to_server(self) -> None:
        server_thread = threading.Thread(target=run_fake_server)
        server_thread.start()

        send_url('https://en.wikipedia.org/wiki/1700')
