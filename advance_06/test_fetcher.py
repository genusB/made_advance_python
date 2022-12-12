import asyncio
import unittest
from io import StringIO
from unittest import mock
import aiohttp
from asynctest import CoroutineMock, patch

from fetcher import read_urls, fetch_url, fetch_batch_urls, worker


class TestFetcher(unittest.IsolatedAsyncioTestCase):

    async def test_read_urls(self):
        urls_queue = asyncio.Queue()
        self.assertTrue(urls_queue.empty())

        await read_urls(urls_queue, 'urls.txt')

        self.assertEqual(urls_queue.qsize(), 100)

    @patch('aiohttp.ClientSession.get')
    @patch('fetcher.get_url_content')
    async def test_fetch_url(self, mock_get, mock_get_url):
        return_content = ''

        mock_get_url.return_value.__aenter__.return_value = CoroutineMock(side_effect=return_content)

        async with aiohttp.ClientSession() as session:
            res = await fetch_url('url', session)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(res, len(return_content))

    @patch('aiohttp.ClientSession.get')
    @mock.patch('fetcher.get_url_content', side_effect=InterruptedError)
    @mock.patch('sys.stdout', new_callable=StringIO)
    async def test_worker(self, mock_get, mock_get_url, mock_print):
        urls_queue = asyncio.Queue()
        await urls_queue.put('url')

        self.assertEqual(urls_queue.qsize(), 1)

        async with aiohttp.ClientSession() as session:
            with self.assertRaises(InterruptedError) as context:
                await worker(urls_queue, session)

        self.assertTrue(urls_queue.empty())
        self.assertEqual(mock_get_url.call_count, 1)


    @patch('aiohttp.ClientSession.get')
    @patch('fetcher.get_url_content')
    @mock.patch('sys.stdout', new_callable=StringIO)
    async def test_fetch_batch_urls(self, mock_get, mock_get_url, mock_print):
        return_content = ''
        number_of_calls = 5
        number_of_workers = 2

        mock_get_url.return_value.__aenter__.return_value = CoroutineMock(side_effect=return_content)

        urls_queue = asyncio.Queue()
        [await urls_queue.put(f'url {i}') for i in range(number_of_calls)]

        self.assertEqual(urls_queue.qsize(), number_of_calls)

        await fetch_batch_urls(urls_queue, number_of_workers)

        self.assertTrue(urls_queue.empty())
        self.assertEqual(mock_get_url.call_count, number_of_calls)
