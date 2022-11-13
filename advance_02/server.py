import queue
from collections import Counter
from string import punctuation
import json
import threading
import socket
import click
from bs4 import BeautifulSoup
import requests


task_queue = queue.Queue()


def process_url(url: str, top_k: int) -> str:
    try:
        request = requests.get(url, timeout=30)
        soup = BeautifulSoup(request.content, features="html.parser")
        text = (''.join(s.findAll(text=True)) for s in soup.findAll(['h1', 'h2', 'h3', 'h4',
                                                                     'h5', 'h6', 'b', 'p',
                                                                     'i', 'strong', 'span', 'em',
                                                                     'blockquote', 'li', 'dt', 'dd']))

        count = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
        count_dict = dict(count.most_common(top_k + 1))

        count_dict.pop("", None)

    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        count_dict = {}

    return json.dumps(count_dict)


def worker(top_k: int) -> None:
    while True:
        url, conn = task_queue.get()
        if url is None or conn is None:
            break
        result = process_url(url, top_k)
        conn.sendall(json.dumps(result).encode())
        task_queue.task_done()


def master(workers: list[threading.Thread]) -> None:
    HOST = '127.0.0.1'
    PORT = 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("socket bound to port", PORT)
        s.listen(100)
        print("socket is listening")
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode() == 'q':
                        stop_workers(workers)
                    task_queue.put((data, conn))


def start_workers(worker_pool: int, top_k: int) -> list[threading.Thread]:
    threads = []
    for _ in range(worker_pool):
        worker_thread = threading.Thread(target=worker,
                                         args=[top_k])
        worker_thread.start()
        threads.append(worker_thread)
    return threads


def stop_workers(threads: list[threading.Thread]) -> None:
    for _ in threads:
        task_queue.put((None, None))
    for thread in threads:
        thread.join()


@click.command(name='server')
@click.option('-w', 'workers_num')
@click.option('-k', 'top_k')
def main(workers_num: int = 5, top_k: int = 10) -> None:
    workers_num = int(workers_num)
    top_k = int(top_k)

    workers = start_workers(workers_num, top_k)

    master_thread = threading.Thread(target=master,
                                     args=[workers]).start()


if __name__ == "__main__":
    main()
