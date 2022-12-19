import pytest


@pytest.mark.parametrize("string, sep, expected_result", [('', '.', ('', '', '')),
                                                          ('', 'a', ('', '', ''))])
def test_empty_string(string, sep, expected_result):
    partition = str.partition(string, sep)

    assert len(partition) == len(expected_result)
    assert all([a == b for a, b in zip(partition, expected_result)])

    assert isinstance(partition, tuple) is True
    assert isinstance(partition[0], str) is True


@pytest.mark.parametrize("string, sep, expected_result", [('12', '.', ('12', '', '')),
                                                          ('qwerty', 'a', ('qwerty', '', ''))])
def test_string_without_sep(string, sep, expected_result):
    partition = str.partition(string, sep)

    assert len(partition) == len(expected_result)
    assert all([a == b for a, b in zip(partition, expected_result)])

    assert isinstance(partition, tuple) is True
    assert isinstance(partition[0], str) is True


@pytest.mark.parametrize("string, sep, expected_result", [('1.2', '.', ('1', '.', '2')),
                                                          ('qwerty', 'r', ('qwe', 'r', 'ty'))])
def test_string_with_one_occurrence_sep(string, sep, expected_result):
    partition = str.partition(string, sep)

    assert len(partition) == len(expected_result)
    assert all([a == b for a, b in zip(partition, expected_result)])

    assert isinstance(partition, tuple) is True
    assert isinstance(partition[0], str) is True


@pytest.mark.parametrize("string, sep, expected_result", [('.1.2.', '.', ('', '.', '1.2.')),
                                                          ('qewerty', 'e', ('q', 'e', 'werty'))])
def test_string_with_several_occurrence_sep(string, sep, expected_result):
    partition = str.partition(string, sep)

    assert len(partition) == len(expected_result)
    assert all([a == b for a, b in zip(partition, expected_result)])

    assert isinstance(partition, tuple) is True
    assert isinstance(partition[0], str) is True


@pytest.mark.parametrize("string, sep, expected_result", [('.1.2.', '.', ('', '.', '1.2.')),
                                                          ('qewerty', 'e', ('q', 'e', 'werty'))])
def test_partition_with_incorrect_arguments(string, sep, expected_result):
    partition = str.partition(string, sep)

    assert len(partition) == len(expected_result)
    assert all([a == b for a, b in zip(partition, expected_result)])

    assert isinstance(partition, tuple) is True
    assert isinstance(partition[0], str) is True


def test_partition_with_empty_separator():
    with pytest.raises(ValueError):
        str.partition('', '')


@pytest.mark.parametrize("incorrect_type_param", [1, 1.34, [1, 2], {1: 2}, (1, 2), lambda x: x + 1])
def test_partition_with_unsupported_types(incorrect_type_param):
    with pytest.raises(TypeError):
        str.partition(incorrect_type_param, '.')

    with pytest.raises(TypeError):
        str.partition('.', incorrect_type_param)
