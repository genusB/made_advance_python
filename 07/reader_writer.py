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
    def read(self, file: typing.TextIO) -> list[str]:
        return file.readlines()


class TxtWriter(BaseWriter):
    def dump(self, data: typing.Union[str, list[str]], file: typing.BinaryIO):
        file.writelines(data)


class JsonReader(BaseReader):
    def read(self, file: typing.TextIO) -> dict:
        return json.load(file)


class JsonWriter(BaseWriter):
    def dump(self, data: dict, file: typing.BinaryIO):
        json.dump(data, file)


class CsvReader(BaseReader):
    def read(self, file: typing.TextIO) -> list[list[str]]:
        rows = [row for row in csv.reader(file)]
        return rows


class CsvWriter(BaseWriter):
    def dump(self, data: list[str], file: typing.BinaryIO):
        writer = csv.writer(file)
        writer.writerows(data)


def read_data(file, reader: BaseReader) -> any:
    return reader.read(file)


def dump_data(data, file, writer: BaseWriter):
    writer.dump(data, file)
