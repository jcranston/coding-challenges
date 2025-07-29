"""
Tests for Longest Common Subsequence solutions.

This module tests both user and canonical implementations using
top-down and bottom-up dynamic programming approaches.
"""

import pytest
from .solution import (
    longest_common_subsequence_user_top_down,
    longest_common_subsequence_user_bottom_up,
    longest_common_subsequence_canonical_top_down,
    longest_common_subsequence_canonical_bottom_up
)

# List of all methods to test
ALL_METHODS = [
    longest_common_subsequence_user_top_down,
    longest_common_subsequence_user_bottom_up,
    longest_common_subsequence_canonical_top_down,
    longest_common_subsequence_canonical_bottom_up
]


def assert_all_methods(text1: str, text2: str, expected: int):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(text1, text2)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "", 0),
        ("a", "", 0),
        ("", "a", 0),
        ("abcba", "abcbcba", 5),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd", 4),
    ]
)
def test_longest_common_subsequence(text1: str, text2: str, expected: int):
    """Test all LCS methods with various input combinations."""
    assert_all_methods(text1, text2, expected)


def test_edge_cases():
    """Test edge cases for all methods."""
    # Single character strings
    assert_all_methods("a", "a", 1)
    assert_all_methods("a", "b", 0)

    # Repeated characters
    assert_all_methods("aaa", "aaa", 3)
    assert_all_methods("aaa", "a", 1)
    assert_all_methods("a", "aaa", 1)

    # Long strings with no common subsequence
    assert_all_methods("abcdef", "ghijkl", 0)

    # Long strings with common subsequence
    assert_all_methods("abcdef", "acef", 4)


def test_leetcode_examples():
    """Test examples from LeetCode problem description."""
    # Example 1: text1 = "abcde", text2 = "ace"
    assert_all_methods("abcde", "ace", 3)

    # Example 2: text1 = "abc", text2 = "abc"
    assert_all_methods("abc", "abc", 3)

    # Example 3: text1 = "abc", text2 = "def"
    assert_all_methods("abc", "def", 0)
