import pytest
from classes_for_int_tests import NumberInt, NumberIndex


@pytest.mark.parametrize("float_num, expected_result", [(1.0, 1),
                                                        (1.2, 1),
                                                        (1.9, 1),
                                                        (0.0, 0),
                                                        (-0.0, 0),
                                                        (-0.1, 0),
                                                        (-1.1, -1)])
def test_float_to_int(float_num, expected_result):
    assert int(float_num) == expected_result
    assert isinstance(int(float_num), int) is True


@pytest.mark.parametrize("str_num, expected_result", [('1', 1),
                                                      ('2', 2),
                                                      ('0', 0),
                                                      ('-0', -0),
                                                      ('-111', -111)])
def test_str_to_int(str_num, expected_result):
    assert int(str_num) == expected_result
    assert isinstance(int(str_num), int) is True


@pytest.mark.parametrize("str_num, base, expected_result", [('0o12', 8, 10),
                                                            ('0b110', 2, 6),
                                                            ('0x1A', 16, 26)])
def test_str_to_int_with_correct_base(str_num, base, expected_result):
    assert int(str_num, base) == expected_result
    assert isinstance(int(str_num, base), int) is True


@pytest.mark.parametrize("num, base", [(0o12, 8),
                                           (0b110, 2),
                                           (0x1A, 16)])
def test_nonstr_to_int_with_base(num, base):
    with pytest.raises(TypeError):
        int(num, base)


@pytest.mark.parametrize("str_num, base", [('0x1A', 3),
                                           ('0o12', 2),
                                           ('0b110', 5)])
def test_str_to_int_with_incorrect_base(str_num, base):
    with pytest.raises(ValueError):
        int(str_num, base)


@pytest.mark.parametrize("incorrect_str_num", ['1.0', 'a'])
def test_incorrect_str_to_int(incorrect_str_num):
    with pytest.raises(ValueError):
        int(incorrect_str_num)


@pytest.mark.parametrize("incorrect_type_param", [[1, 2], {1: 2}, (1, 2), lambda x: x + 1])
def test_not_supported_types_to_int(incorrect_type_param):
    with pytest.raises(TypeError):
        int(incorrect_type_param)


def test_class_with_int_magic_method():
    data = NumberInt()

    assert int(data) == data.value
    assert isinstance(int(data), int) is True


def test_class_with_index_magic_method():
    data = NumberIndex()

    assert int(data) == data.value
    assert isinstance(int(data), int) is True
