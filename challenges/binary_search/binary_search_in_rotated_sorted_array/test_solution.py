from .solution import (
    binary_search_in_rotated_sorted_array_canonical,
    binary_search_in_rotated_sorted_array_user,
)


def test_binary_search_in_rotated_sorted_array():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    expected = 4
    for solution in [
        binary_search_in_rotated_sorted_array_user,
        binary_search_in_rotated_sorted_array_canonical,
    ]:
        assert solution(nums, target) == expected

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1
    for solution in [
        binary_search_in_rotated_sorted_array_user,
        binary_search_in_rotated_sorted_array_canonical,
    ]:
        assert solution(nums, target) == expected

    nums = [1]
    target = 0
    expected = -1
    for solution in [
        binary_search_in_rotated_sorted_array_user,
        binary_search_in_rotated_sorted_array_canonical,
    ]:
        assert solution(nums, target) == expected

    nums = [1, 3]
    target = 3
    expected = 1
    for solution in [
        binary_search_in_rotated_sorted_array_user,
        binary_search_in_rotated_sorted_array_canonical,
    ]:
        assert solution(nums, target) == expected
