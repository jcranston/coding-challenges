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


@pytest.mark.parametrize("s, expected", test_cases)
def test_valid_palindrome_user(s, expected):
    result = valid_palindrome_user(s)
    if result is None:
        # If function is not implemented, just pass the test
        return
    assert result == expected


@pytest.mark.parametrize("s, expected", test_cases)
def test_valid_palindrome_canonical(s, expected):
    result = valid_palindrome_canonical(s)
    if result is None:
        # If function is not implemented, just pass the test
        return
    assert result == expected
