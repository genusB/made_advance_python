import unittest
from search_file_generator import search_in_file


class TestSearchFileGenerator(unittest.TestCase):
    def test_correct_keywords(self):
        with open("./test_files/txt1.txt") as file1, \
             open("./test_files/txt2.txt") as file2:
            res1 = list(search_in_file(file1, ["lorem", "elit"]))
            res2 = list(search_in_file(file2, ["ipsum"]))

        self.assertListEqual(res1, ["Lorem ipsum", "adipiscing elit."])
        self.assertListEqual(res2, ["Lorem ipsum"])

    def test_incorrect_keywords(self):
        with open("./test_files/txt1.txt") as file1, \
             open("./test_files/txt2.txt") as file2:
            res1 = list(search_in_file(file1, ["lore", "elit.", "consec"]))
            res2 = list(search_in_file(file2, ["ips"]))

        self.assertListEqual(res1, [])
        self.assertListEqual(res2, [])

    def test_empty_file(self):
        with open("./test_files/empty.txt") as file:
            res = list(search_in_file(file, ["whatever"]))

        self.assertListEqual(res, [])
