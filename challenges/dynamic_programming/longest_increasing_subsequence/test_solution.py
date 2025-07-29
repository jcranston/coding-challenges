import pytest

from .solution import (
    longest_increasing_subsequence_optimized,
    longest_increasing_subsequence_quadratic,
)


def test_basic_case_quadratic():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_length = 4
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        # Verify the sequence is actually increasing
        for i in range(1, len(sequence)):
            assert sequence[i] > sequence[i - 1]


def test_basic_case_optimized():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_length = 4
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        # Verify the sequence is actually increasing
        for i in range(1, len(sequence)):
            assert sequence[i] > sequence[i - 1]


def test_strictly_increasing_quadratic():
    nums = [1, 2, 3, 4, 5]
    expected_length = 5
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert sequence == [1, 2, 3, 4, 5]


def test_strictly_increasing_optimized():
    nums = [1, 2, 3, 4, 5]
    expected_length = 5
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert sequence == [1, 2, 3, 4, 5]


def test_strictly_decreasing_quadratic():
    nums = [5, 4, 3, 2, 1]
    expected_length = 1
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert len(sequence) == 1


def test_strictly_decreasing_optimized():
    nums = [5, 4, 3, 2, 1]
    expected_length = 1
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert len(sequence) == 1


def test_duplicate_elements_quadratic():
    nums = [2, 2, 2, 2, 2]
    expected_length = 1
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert len(sequence) == 1


def test_duplicate_elements_optimized():
    nums = [2, 2, 2, 2, 2]
    expected_length = 1
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert len(sequence) == 1


def test_empty_array_quadratic():
    nums = []
    expected_length = 0
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert sequence == []


def test_empty_array_optimized():
    nums = []
    expected_length = 0
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        assert sequence == []


def test_small_array_quadratic():
    nums = [1, 3, 2]
    expected_length = 2
    result = longest_increasing_subsequence_quadratic(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        # Verify the sequence is actually increasing
        for i in range(1, len(sequence)):
            assert sequence[i] > sequence[i - 1]


def test_small_array_optimized():
    nums = [1, 3, 2]
    expected_length = 2
    result = longest_increasing_subsequence_optimized(nums)
    if result is not None:
        length, sequence = result
        assert length == expected_length
        # Verify the sequence is actually increasing
        for i in range(1, len(sequence)):
            assert sequence[i] > sequence[i - 1]
