import asyncio
import aiofiles as aiofiles
import aiohttp
import click


async def get_url_content(resp):
    return await resp.read()


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await get_url_content(resp)
        return len(data)


async def worker(queue, session):
    while True:
        url = await queue.get()

        try:
            res = 'error'
            res = await fetch_url(url, session)
        finally:
            print(res)
            queue.task_done()


async def fetch_batch_urls(queue, workers):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(queue, session))
            for _ in range(workers)
        ]
        await queue.join()

        for task in tasks:
            task.cancel()


async def read_urls(urls_queue, urls_path):
    async with aiofiles.open(urls_path, mode='r') as file:
        async for url in file:
            await urls_queue.put(url)


async def fetcher(workers_num, urls_path):
    workers_num = int(workers_num)

    urls_queue = asyncio.Queue()

    await read_urls(urls_queue, urls_path)

    await fetch_batch_urls(urls_queue, workers_num)


@click.command(name='fetcher')
@click.argument('workers_num')
@click.argument('urls_path')
def main(workers_num, urls_path):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetcher(workers_num, urls_path))


if __name__ == '__main__':
    main()
