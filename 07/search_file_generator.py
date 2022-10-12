import typing


def search_in_file(file: typing.TextIO, keywords: list[str]):
    for line in file.readlines():
        line = line.strip()
        modified_line = line.lower().replace(".", "").replace(",", "")
        if any(keyword.lower() in modified_line.split() for keyword in keywords):
            yield line
