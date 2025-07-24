import pytest

from .solution import reverse_vowels_canonical, reverse_vowels_user

test_cases = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
    ("aA", "Aa"),
    ("bcd", "bcd"),
    ("aeiou", "uoiea"),
]


@pytest.mark.parametrize("s,expected", test_cases)
def test_reverse_vowels_user(s, expected):
    assert reverse_vowels_user(s) == expected


@pytest.mark.parametrize("s,expected", test_cases)
def test_reverse_vowels_canonical(s, expected):
    assert reverse_vowels_canonical(s) == expected
