import threading
import unittest
import json
import socket
import time
from io import StringIO
from unittest.mock import patch, Mock

from server import process_url, worker, master, start_workers, stop_workers, task_queue


def fake_quit_client(host: str = '127.0.0.1', port: int = 3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(b'q')


class TestServer(unittest.TestCase):

    def test_process_url(self) -> None:
        existent_url: str = 'https://en.wiktionary.org/wiki/Wiktionary:Welcome,_newcomers'
        top_k: int = 2
        res: str = process_url(existent_url, top_k)
        res_to_dict: dict = json.loads(res)

        self.assertEqual(res, '{"in": 31, "to": 28}')
        self.assertIsInstance(res_to_dict, dict)
        self.assertEqual(len(res_to_dict), top_k)

    def test_process_inexistent_url(self) -> None:
        inexistent_url: str = 'https://dkkdkd.com/'
        top_k: int = 10

        self.assertEqual(process_url(inexistent_url, top_k), '{}')

    def test_start_workers(self) -> None:
        worker_pool: int = 5
        top_k: int = 10
        threads: list[threading.Thread] = start_workers(worker_pool, top_k)

        self.assertEqual(len(threads), worker_pool)
        self.assertIsInstance(threads[0], threading.Thread)

        stop_workers(threads)

    @patch('sys.stdout', new_callable=StringIO)
    def test_master(self, mock_print: Mock):
        worker_pool: int = 5
        top_k: int = 10
        threads: list[threading.Thread] = start_workers(worker_pool, top_k)

        try:
            server_thread: threading.Thread = threading.Thread(target=master, args=[threads])
            server_thread.start()

            time.sleep(0.1)

            fake_quit_client()

        except Exception as e:
            self.fail()

        actual_val: str = mock_print.getvalue()
        expected_val: str = "socket bound to port 3000\nsocket is listening\n"

        self.assertEqual(actual_val, expected_val)
