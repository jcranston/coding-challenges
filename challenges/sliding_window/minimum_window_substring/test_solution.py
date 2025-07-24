import pytest

from .solution import min_window_substring_canonical, min_window_substring_user

test_cases = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("abc", "d", ""),
    ("abdecfab", "abc", "cfab"),
]


@pytest.mark.parametrize("s, t, expected", test_cases)
def test_min_window_substring(s, t, expected):
    for solution in [min_window_substring_user, min_window_substring_canonical]:
        assert solution(s, t) == expected
