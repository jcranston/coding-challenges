import pytest

from .solution import valid_palindrome_canonical, valid_palindrome_user

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    (" ", True),
    ("0P", False),
    ("abccba", True),
]


@pytest.mark.parametrize("s,expected", test_cases)
def test_valid_palindrome_user(s, expected):
    assert valid_palindrome_user(s) == expected


@pytest.mark.parametrize("s,expected", test_cases)
def test_valid_palindrome_canonical(s, expected):
    assert valid_palindrome_canonical(s) == expected
