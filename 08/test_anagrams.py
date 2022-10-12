import unittest
from anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):
    def test_with_matches(self):
        text = 'loremmorelromel'
        pattern = 'oreml'
        self.assertListEqual(find_anagrams(text, pattern), [0, 5, 8, 9])

        text = 'abbbacabacaba'
        pattern = 'ab'
        self.assertListEqual(find_anagrams(text, pattern), [0, 3, 6, 7, 10])

    def test_without_matches(self):
        text = 'bbbbb'
        pattern = 'aaa'

        self.assertListEqual(find_anagrams(text, pattern), [])

    def test_with_empty_text(self):
        text = ''
        pattern = 'a'

        self.assertListEqual(find_anagrams(text, pattern), [])

    def test_with_empty_pattern(self):
        text = 'aaa'
        pattern = ''

        self.assertListEqual(find_anagrams(text, pattern), [0, 1, 2])