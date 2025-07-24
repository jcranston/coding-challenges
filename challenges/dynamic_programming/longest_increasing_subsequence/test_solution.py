import pytest

from .solution import (
    longest_increasing_subsequence_optimized,
    longest_increasing_subsequence_quadratic,
)


def test_basic_case_quadratic():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected = (4, [2, 3, 7, 18])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_basic_case_optimized():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected = (4, [2, 3, 7, 18])
    assert longest_increasing_subsequence_optimized(nums) == expected


def test_strictly_increasing_quadratic():
    nums = [1, 2, 3, 4, 5]
    expected = (5, [1, 2, 3, 4, 5])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_strictly_increasing_optimized():
    nums = [1, 2, 3, 4, 5]
    expected = (5, [1, 2, 3, 4, 5])
    assert longest_increasing_subsequence_optimized(nums) == expected


def test_strictly_decreasing_quadratic():
    nums = [5, 4, 3, 2, 1]
    expected = (1, [1])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_strictly_decreasing_optimized():
    nums = [5, 4, 3, 2, 1]
    expected = (1, [1])
    assert longest_increasing_subsequence_optimized(nums) == expected


def test_duplicate_elements_quadratic():
    nums = [2, 2, 2, 2, 2]
    expected = (1, [2])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_duplicate_elements_optimized():
    nums = [2, 2, 2, 2, 2]
    expected = (1, [2])
    assert longest_increasing_subsequence_optimized(nums) == expected


def test_empty_array_quadratic():
    nums = []
    expected = (0, [])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_empty_array_optimized():
    nums = []
    expected = (0, [])
    assert longest_increasing_subsequence_optimized(nums) == expected


def test_small_array_quadratic():
    nums = [1, 3, 2]
    expected = (2, [1, 2])
    assert longest_increasing_subsequence_quadratic(nums) == expected


def test_small_array_optimized():
    nums = [1, 3, 2]
    expected = (2, [1, 2])
    assert longest_increasing_subsequence_optimized(nums) == expected
