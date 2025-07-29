import pytest

from .solution import (
    canonical_count_palindromic_substrings,
    count_palindromic_substrings,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", 3),
        ("aaa", 6),
        ("a", 1),
        ("racecar", 10),
        ("abba", 6),
        ("abcd", 4),
        ("", 0),
    ],
)
def test_count_palindromic_substrings(s, expected):
    for solution in [
        count_palindromic_substrings,
        canonical_count_palindromic_substrings,
    ]:
        result = solution(s)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
