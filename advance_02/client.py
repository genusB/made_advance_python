import concurrent.futures
import json
import socket
from typing import Iterator
import click


def send_url(url: str, host: str = '127.0.0.1', port: int = 3000) -> dict:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(str.encode(url))
        response: bytes = client_socket.recv(1024)

        if response:
            result: dict = json.loads(response)
            return result


def send_urls(workers_num: int, urls: list[str]) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers_num) as executor:
        responses: Iterator[dict] = executor.map(send_url, urls)

        for url, response in zip(urls, responses):
            if response:
                print(f'{url}: {response}')


def read_url_file(urls_file_path: str) -> list[str]:
    with open(urls_file_path, encoding="utf-8") as file:
        urls: list[str] = file.read().splitlines()

    return urls


@click.command(name='client')
@click.argument('workers_num')
@click.argument('urls_file_path')
def main(workers_num: int, urls_file_path: str) -> None:
    workers_num: int = int(workers_num)

    urls: list[str] = read_url_file(urls_file_path)

    send_urls(workers_num, urls)


if __name__ == "__main__":
    main()
