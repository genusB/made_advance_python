import json
import threading
import unittest
import socket
from io import StringIO
from unittest.mock import patch, Mock
from client import read_url_file, send_urls, send_url


def run_fake_simple_server(host: str = '127.0.0.1', port: int = 3001) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(json.dumps({data.decode(): 200}).encode())


def run_fake_server(host: str = '127.0.0.1', port: int = 3000) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data or data.decode() == 'q':
                        break
                    conn.sendall(json.dumps({data.decode(): 200}).encode())
                if data and data.decode() == 'q':
                    break


class TestClient(unittest.TestCase):

    def test_read_url_file(self) -> None:
        self.assertTrue(read_url_file('./test_files/test_urls.txt'), ['https://en.wikipedia.org/wiki/1700', 'q'])

    def test_send_url(self) -> None:
        server_thread = threading.Thread(target=run_fake_simple_server)
        server_thread.start()

        URL = 'https://en.wikipedia.org/wiki/1700'
        result = send_url(URL, port=3001)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {URL: 200})

    @patch('sys.stdout', new_callable=StringIO)
    def test_send_urls(self, mock_print: Mock) -> None:
        number_of_workers = 2
        urls = read_url_file('./test_files/test_urls2.txt')

        server_thread = threading.Thread(target=run_fake_server)
        server_thread.start()

        send_urls(number_of_workers, urls)
        actual_val = mock_print.getvalue()
        expected_val = f"{urls[0]}: {{'{urls[0]}': 200}}\n{urls[1]}: {{'{urls[1]}': 200}}\n"
        self.assertEqual(actual_val, expected_val)
