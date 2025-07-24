from .solution import (  # minimum_size_subarray_sum_canonical,
    minimum_size_subarray_sum_user,
)


def test_minimum_size_subarray_sum_basic():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = (2, [4, 3])
    for solution in [
        minimum_size_subarray_sum_user,
        # minimum_size_subarray_sum_canonical,
    ]:
        assert solution(target, nums) == expected


def test_minimum_size_subarray_sum_single_element():
    target = 4
    nums = [1, 4, 4]
    expected = (1, [4])
    for solution in [
        minimum_size_subarray_sum_user,
        # minimum_size_subarray_sum_canonical,
    ]:
        assert solution(target, nums) == expected


def test_minimum_size_subarray_sum_no_valid_subarray():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = (0, [])
    for solution in [
        minimum_size_subarray_sum_user,
        # minimum_size_subarray_sum_canonical,
    ]:
        assert solution(target, nums) == expected


def test_minimum_size_subarray_sum_entire_array():
    target = 15
    nums = [1, 2, 3, 4, 5]
    expected = (5, [1, 2, 3, 4, 5])
    for solution in [
        minimum_size_subarray_sum_user,
        # minimum_size_subarray_sum_canonical,
    ]:
        assert solution(target, nums) == expected
