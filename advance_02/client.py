import concurrent.futures
import json
import socket
import click


def send_url(url: str, host: str = '127.0.0.1', port: int = 3000) -> dict:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str.encode(url))
        response = s.recv(1024)
        if response:
            result = json.loads(response)
            return result


def send_urls(workers_num: int, urls: list[str]) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers_num) as executor:
        responses = executor.map(send_url, urls)

        for url, response in zip(urls, responses):
            if response:
                print(f'{url}: {response}')


def read_url_file(urls_file_path: str):
    with open(urls_file_path, encoding="utf-8") as file:
        urls = file.read().splitlines()
    return urls


@click.command(name='client')
@click.argument('workers_num')
@click.argument('urls_file_path')
def main(workers_num: int, urls_file_path: str) -> None:
    workers_num = int(workers_num)
    urls = read_url_file(urls_file_path)
    send_urls(workers_num, urls)


if __name__ == "__main__":
    main()