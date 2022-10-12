import typing


def find_anagrams(text: str, pattern: str) -> list[int]:
    symbols_number = 26
    text = text.lower().replace(' ', '')
    pattern = pattern.lower().replace(' ', '')
    indexes_of_anagrams = []

    pattern_freq = [0] * symbols_number

    for symbol in pattern:
        index = ord(symbol) - ord('a')
        pattern_freq[index] += 1

    for i in range(len(text) - len(pattern)):
        j = i
        str_freq = [0] * symbols_number
        while j < i + len(pattern):
            index = ord(text[j]) - ord('a')
            str_freq[index] += 1
            j += 1
        if is_equal(str_freq, pattern_freq):
            indexes_of_anagrams.append(i)

    return indexes_of_anagrams


def is_equal(seq1, seq2):
    if len(seq1) != len(seq2):
        return False
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            return False

    return True
