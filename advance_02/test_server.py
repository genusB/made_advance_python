import unittest
import json
from server import process_url, worker, master, start_workers, stop_workers


class TestServer(unittest.TestCase):

    def test_process_url(self) -> None:
        existent_url = 'https://en.wiktionary.org/wiki/Wiktionary:Welcome,_newcomers'
        top_k = 2
        res = process_url(existent_url, top_k)
        self.assertEqual(res, '{"in": 31, "to": 28}')
        res_to_dict = json.loads(res)
        self.assertIsInstance(res_to_dict, dict)
        self.assertEqual(len(res_to_dict), top_k)

    def test_process_inexistent_url(self) -> None:
        inexistent_url = 'https://dkkdkd.com/'
        top_k = 10
        self.assertEqual(process_url(inexistent_url, top_k), '{}')
