import pytest

from .solution import (
    median_of_two_sorted_arrays_canonical,
    median_of_two_sorted_arrays_user,
)


def test_odd_total_length():
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    result_user = median_of_two_sorted_arrays_user(nums1, nums2)
    if result_user is not None:
        assert result_user == expected
    result_canonical = median_of_two_sorted_arrays_canonical(nums1, nums2)
    if result_canonical is not None:
        assert result_canonical == expected


def test_even_total_length():
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    result_user = median_of_two_sorted_arrays_user(nums1, nums2)
    if result_user is not None:
        assert result_user == expected
    result_canonical = median_of_two_sorted_arrays_canonical(nums1, nums2)
    if result_canonical is not None:
        assert result_canonical == expected


def test_one_empty():
    nums1 = []
    nums2 = [1]
    expected = 1.0
    result_user = median_of_two_sorted_arrays_user(nums1, nums2)
    if result_user is not None:
        assert result_user == expected
    result_canonical = median_of_two_sorted_arrays_canonical(nums1, nums2)
    if result_canonical is not None:
        assert result_canonical == expected


def test_both_nonempty_different_lengths():
    nums1 = [1, 3, 5]
    nums2 = [2, 4]
    expected = 3.0
    result_user = median_of_two_sorted_arrays_user(nums1, nums2)
    if result_user is not None:
        assert result_user == expected
    result_canonical = median_of_two_sorted_arrays_canonical(nums1, nums2)
    if result_canonical is not None:
        assert result_canonical == expected
