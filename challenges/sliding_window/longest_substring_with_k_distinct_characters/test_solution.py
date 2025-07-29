"""Tests for Longest Substring with K Distinct Characters problem."""

import pytest

from .solution import (
    longest_substring_with_k_distinct_canonical,
    longest_substring_with_k_distinct_user,
)

# List of all methods to test
ALL_METHODS = [
    longest_substring_with_k_distinct_user,
    longest_substring_with_k_distinct_canonical,
]


def assert_all_methods(s: str, k: int, expected: int):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(s, k)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("eceba", 2, 3),  # "ece" has 2 distinct characters
        ("aa", 1, 2),  # "aa" has 1 distinct character
        ("eceba", 1, 1),  # Any single character substring
        ("eceba", 3, 4),  # "eceb" has 3 distinct characters
        ("", 1, 0),  # Empty string
        ("a", 1, 1),  # Single character
        ("aa", 2, 2),  # All characters are the same
        ("abc", 1, 1),  # Only one distinct character allowed
        ("abc", 2, 2),  # Two distinct characters allowed
        ("abc", 3, 3),  # All three distinct characters allowed
    ],
)
def test_longest_substring_with_k_distinct(s: str, k: int, expected: int):
    """Test various cases for longest substring with k distinct characters."""
    assert_all_methods(s, k, expected)


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test with k = 0 (should return 0)
    assert_all_methods("abc", 0, 0)

    # Test with very large k
    assert_all_methods("abc", 10, 3)

    # Test with repeated characters
    assert_all_methods("aaaa", 1, 4)
    assert_all_methods("aaaa", 2, 4)

    # Test with alternating characters
    assert_all_methods("abab", 1, 1)
    assert_all_methods("abab", 2, 4)
