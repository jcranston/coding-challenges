import pytest

from .solution import find_all_anagrams_canonical, find_all_anagrams_user

test_cases = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("a", "a", [0]),
    ("a", "b", []),
    ("baa", "aa", [1]),
]


@pytest.mark.parametrize("s, p, expected", test_cases)
def test_find_all_anagrams(s, p, expected):
    for solution in [find_all_anagrams_user, find_all_anagrams_canonical]:
        result = solution(s, p)
        assert sorted(result) == sorted(expected)
