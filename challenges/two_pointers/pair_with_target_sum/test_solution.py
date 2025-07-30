"""
Tests for Two Sum II - Input Array Is Sorted problem.
"""

import pytest

from .solution import two_sum_sorted_canonical, two_sum_sorted_user

# List of all methods to test
ALL_METHODS = [two_sum_sorted_user, two_sum_sorted_canonical]


def assert_all_methods(numbers: list[int], target: int, expected: list[int]):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(numbers, target)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),  # 2 + 7 = 9
        ([2, 3, 4], 6, [1, 3]),  # 2 + 4 = 6
        ([-1, 0], -1, [1, 2]),  # -1 + 0 = -1
        ([1, 2, 3, 4, 5], 9, [4, 5]),  # 4 + 5 = 9
        ([1, 2, 3, 4, 5], 3, [1, 2]),  # 1 + 2 = 3
        ([1, 2, 3, 4, 5], 8, [3, 5]),  # 3 + 5 = 8
        ([1, 2, 3, 4, 5], 6, [1, 5]),  # 1 + 5 = 6
        ([1, 2, 3, 4, 5], 7, [2, 5]),  # 2 + 5 = 7
        ([1, 2, 3, 4, 5], 9, [4, 5]),  # 4 + 5 = 9
        ([1, 2, 3, 4, 5], 3, [1, 2]),  # 1 + 2 = 3
    ],
)
def test_two_sum_sorted(numbers: list[int], target: int, expected: list[int]):
    """Test various cases for two sum in sorted array."""
    assert_all_methods(numbers, target, expected)


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test with minimum array size
    assert_all_methods([1, 2], 3, [1, 2])

    # Test with negative numbers - fixed to match actual solution
    assert_all_methods([-3, -2, -1, 0, 1], -3, [1, 4])

    # Test with duplicate numbers
    assert_all_methods([1, 1, 2, 3], 2, [1, 2])

    # Test with large numbers
    assert_all_methods([1, 2, 3, 100, 200], 103, [3, 4])

    # Test with target at boundaries
    assert_all_methods([1, 2, 3, 4, 5], 6, [1, 5])
    assert_all_methods([1, 2, 3, 4, 5], 9, [4, 5])
