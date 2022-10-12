import json
import csv
import typing


class BaseReader:
    def read(self, file: typing.TextIO) -> any:
        pass


class BaseWriter:
    def dump(self, data, file: typing.BinaryIO):
        pass


class TxtReader(BaseReader):
    def read(self, file) -> list[str]:
        return file.readlines()


class TxtWriter(BaseWriter):
    def dump(self, data: typing.Union[str, list[str]], file):
        file.writelines(data)


class JsonReader(BaseReader):
    def read(self, file) -> json:
        return json.load(file)


class JsonWriter(BaseWriter):
    def dump(self, data: dict, file):
        json.dump(data, file)


class CsvReader(BaseReader):
    def read(self, file) -> list[list[str]]:
        rows = [row for row in csv.reader(file)]
        return rows


class CsvWriter(BaseWriter):
    def dump(self, data: list[str], file):
        writer = csv.writer(file)
        writer.writerows(data)


def read_data(file, reader: BaseReader):
    return reader.read(file)


def dump_data(data, file, writer: BaseWriter):
    writer.dump(data, file)
