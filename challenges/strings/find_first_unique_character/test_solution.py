from .solution import find_first_unique_character


def test_example_1():
    assert find_first_unique_character("adobe") == 0


def test_example_2():
    assert find_first_unique_character("leetcode") == 0


def test_example_3():
    assert find_first_unique_character("aabb") == -1


def test_middle_unique():
    assert find_first_unique_character("aabbc") == 4


def test_last_unique():
    assert find_first_unique_character("aabbccz") == 6


def test_all_unique():
    assert find_first_unique_character("abc") == 0


def test_long_string():
    s = "a" * 10000 + "b" + "a" * 10000
    assert find_first_unique_character(s) == 10000
