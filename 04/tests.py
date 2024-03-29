from custom_list import CustomList


def check_equality(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def custom_list_test():
    custom_list1 = CustomList([1, 2, 3])
    custom_list2 = CustomList([3, 2, 1])
    custom_list3 = CustomList([5, 6, 7, 8])
    custom_empty_list = CustomList([])

    assert custom_list1 == custom_list2
    assert not custom_list1 == custom_list3
    assert not custom_list1 == custom_empty_list

    assert custom_list1 != custom_list3
    assert not custom_list1 != custom_list2

    assert custom_list1 >= custom_list2
    assert custom_list3 >= custom_list2
    assert not custom_list2 >= custom_list3

    assert custom_list3 > custom_list2
    assert not custom_list2 > custom_list3

    assert custom_list1 <= custom_list2
    assert custom_list2 <= custom_list3
    assert not custom_list3 <= custom_list2

    assert custom_list2 < custom_list3
    assert not custom_list3 < custom_list2

    assert str(custom_list1) == "1 2 3 6"
    assert str(custom_empty_list) == "0"

    sub_of_equal_len = custom_list2 - custom_list1
    sub_of_unequal_len1 = custom_list3 - custom_list1
    sub_of_unequal_len2 = custom_list1 - custom_list3
    sub_of_unequal_len3 = custom_list1 - custom_empty_list
    sub_of_unequal_len4 = custom_empty_list - custom_list1

    assert isinstance(sub_of_equal_len, CustomList) and check_equality(sub_of_equal_len, [2, 0, -2])
    assert check_equality(custom_list1, [1, 2, 3]) and check_equality(custom_list2, [3, 2, 1])
    assert isinstance(sub_of_unequal_len1, CustomList) and check_equality(sub_of_unequal_len1, [4, 4, 4, 8])
    assert isinstance(sub_of_unequal_len2, CustomList) and check_equality(sub_of_unequal_len2, [-4, -4, -4, -8])
    assert isinstance(sub_of_unequal_len3, CustomList) and check_equality(sub_of_unequal_len3, [1, 2, 3])
    assert isinstance(sub_of_unequal_len4, CustomList) and check_equality(sub_of_unequal_len4, [-1, -2, -3])

    list1 = [5, 6, 7]
    list2 = [5, 6, 7, 8]

    sub_of_equal_len_with_list1 = custom_list1 - list1
    sub_of_equal_len_with_list2 = list1 - custom_list1
    sub_of_unequal_len_with_list1 = custom_list1 - list2
    sub_of_unequal_len_with_list2 = list2 - custom_list1

    assert isinstance(sub_of_equal_len_with_list1, CustomList) and check_equality(sub_of_equal_len_with_list1, [-4, -4, -4])
    assert check_equality(custom_list1, [1, 2, 3]) and check_equality(list1, [5, 6, 7])
    assert isinstance(sub_of_equal_len_with_list2, CustomList) and check_equality(sub_of_equal_len_with_list2, [4, 4, 4])
    assert isinstance(sub_of_unequal_len_with_list1, CustomList) and check_equality(sub_of_unequal_len_with_list1, [-4, -4, -4, -8])
    assert isinstance(sub_of_unequal_len_with_list2, CustomList) and check_equality(sub_of_unequal_len_with_list2, [4, 4, 4, 8])

    add_of_equal_len1 = custom_list2 + custom_list1
    add_of_equal_len2 = custom_list1 + custom_list2
    add_of_unequal_len1 = custom_list3 + custom_list1
    add_of_unequal_len2 = custom_list1 + custom_list3
    add_of_unequal_len3 = custom_list1 + custom_empty_list

    assert isinstance(add_of_equal_len1, CustomList) and check_equality(add_of_equal_len1, [4, 4, 4])
    assert check_equality(custom_list1, [1, 2, 3]) and check_equality(custom_list2, [3, 2, 1])
    assert isinstance(add_of_equal_len2, CustomList) and check_equality(add_of_equal_len2, [4, 4, 4])
    assert isinstance(add_of_unequal_len1, CustomList) and check_equality(add_of_unequal_len1, [6, 8, 10, 8])
    assert isinstance(add_of_unequal_len2, CustomList) and check_equality(add_of_unequal_len2, [6, 8, 10, 8])
    assert isinstance(add_of_unequal_len3, CustomList) and check_equality(add_of_unequal_len3, [1, 2, 3])

    add_of_equal_len_with_list1 = custom_list1 + list1
    add_of_equal_len_with_list2 = list1 + custom_list1
    add_of_unequal_len_with_list1 = custom_list1 + list2
    add_of_unequal_len_with_list2 = list2 + custom_list1

    assert isinstance(add_of_equal_len_with_list1, CustomList) and add_of_equal_len_with_list1 == [6, 8, 10]
    assert check_equality(custom_list1, [1, 2, 3]) and check_equality(list1, [5, 6, 7])
    assert isinstance(add_of_equal_len_with_list2, CustomList) and check_equality(add_of_equal_len_with_list2, [6, 8, 10])
    assert isinstance(add_of_unequal_len_with_list1, CustomList) and check_equality(add_of_unequal_len_with_list1, [6, 8, 10, 8])
    assert isinstance(add_of_unequal_len_with_list2, CustomList) and check_equality(add_of_unequal_len_with_list2, [6, 8, 10, 8])


custom_list_test()
