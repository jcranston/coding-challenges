from .solution import find_minimum_in_rotated_sorted_array


def test_find_minimum_in_rotated_sorted_array_example():
    assert find_minimum_in_rotated_sorted_array([3, 4, 5, 1, 2]) == 1
    assert find_minimum_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_minimum_in_rotated_sorted_array([11, 13, 15, 17]) == 11
    assert find_minimum_in_rotated_sorted_array([2, 1]) == 1
