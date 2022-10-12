import json
import unittest
import reader_writer as rw


class TestReaderWriter(unittest.TestCase):
    def test_text_reader(self):
        with open("./test_files/txt1.txt") as file:
            data_from_reader = rw.read_data(file, reader=rw.TxtReader())

        with open("./test_files/txt1.txt") as file:
            actual_data = file.readlines()

        self.assertEqual(data_from_reader, actual_data)

        with open("./test_files/txt2.txt") as file:
            data_from_reader = rw.read_data(file, reader=rw.TxtReader())

        with open("./test_files/txt2.txt") as file:
            actual_data = file.readlines()

        self.assertEqual(data_from_reader, actual_data)

    def test_text_writer(self):
        with open("./test_files/txt_writer.txt", "w+") as file:
            rw.dump_data("hello darkness", file, writer=rw.TxtWriter())

        with open("./test_files/txt_writer.txt") as file:
            data = rw.read_data(file, reader=rw.TxtReader())

        self.assertEqual(data, ["hello darkness"])

        with open("./test_files/txt_writer2.txt", "w+") as file, \
             open("./test_files/txt1.txt") as file2:
            actual_data = file2.readlines()
            rw.dump_data(actual_data, file, writer=rw.TxtWriter())

        with open("./test_files/txt_writer2.txt") as file:
            data = rw.read_data(file, reader=rw.TxtReader())

        self.assertEqual(data, actual_data)

    def test_json_reader(self):
        with open("./test_files/json1.json") as file, \
             open("test_files/json2.txt") as file2:
            data_from_reader = rw.read_data(file, reader=rw.JsonReader())
            actual_data = file2.readline()

        self.assertEqual(str(data_from_reader), actual_data)
        self.assertIsInstance(data_from_reader, object)

    def test_json_writer(self):
        dictionary = {"x": 10, "val": 12}
        with open("./test_files/json_writer.json", "w+") as file:
            rw.dump_data(dictionary, file, writer=rw.JsonWriter())

        with open("./test_files/json_writer.json") as file:
            data = rw.read_data(file, reader=rw.JsonReader())

        self.assertEqual(data, dictionary)
        self.assertIsInstance(data, dict)

        with open("./test_files/json_writer.json", "w+") as file, \
             open("./test_files/json1.json") as file2:
            dictionary = json.load(file2)
            rw.dump_data(dictionary, file, writer=rw.JsonWriter())

        with open("./test_files/json_writer.json") as file:
            data = rw.read_data(file, reader=rw.JsonReader())

        self.assertEqual(data, dictionary)
        self.assertIsInstance(data, dict)

    def test_csv_reader(self):
        with open("./test_files/name.csv") as file:
            data_from_reader = rw.read_data(file, reader=rw.CsvReader())

        actual_data = [["Name", "Surname"]]
        self.assertListEqual(data_from_reader, actual_data)

    def test_csv_writer(self):
        with open("./test_files/addresses.csv") as file, \
             open("./test_files/addresses2.csv", "w+") as file2:
            data_from_reader = rw.read_data(file, reader=rw.CsvReader())
            rw.dump_data(data_from_reader, file2, writer=rw.CsvWriter())

        with open("./test_files/addresses2.csv") as file:
            data_from_writer = rw.read_data(file, reader=rw.CsvReader())

        self.assertListEqual(data_from_reader, data_from_writer)
