"""Tests for Squaring a Sorted Array problem."""

import pytest

from .solution import (
    square_sorted_array_binary_search,
    square_sorted_array_canonical,
    square_sorted_array_user,
)

ALL_METHODS = [
    square_sorted_array_user,
    square_sorted_array_canonical,
    square_sorted_array_binary_search,
]


def assert_all_methods(nums: list[int], expected: list[int]):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(nums)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        ([-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]),
        ([0, 1, 2, 3, 4], [0, 1, 4, 9, 16]),
        ([-2, -1, 0, 1, 2], [0, 1, 1, 4, 4]),
        ([], []),
        ([1], [1]),
        ([-1], [1]),
        ([0], [0]),
    ],
)
def test_square_sorted_array(nums: list[int], expected: list[int]):
    """Test various cases for squaring sorted array."""
    assert_all_methods(nums, expected)


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test with single element
    assert_all_methods([5], [25])
    assert_all_methods([-5], [25])
    assert_all_methods([0], [0])

    # Test with all negative numbers
    assert_all_methods([-3, -2, -1], [1, 4, 9])

    # Test with all positive numbers
    assert_all_methods([1, 2, 3], [1, 4, 9])

    # Test with mixed positive and negative
    assert_all_methods([-3, -1, 0, 2, 4], [0, 1, 4, 9, 16])
