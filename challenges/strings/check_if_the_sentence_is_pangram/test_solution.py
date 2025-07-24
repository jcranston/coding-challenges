import pytest

from .solution import check_if_pangram_canonical, check_if_pangram_user

test_cases = [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("", False),
    ("abcde fghij klmno pqrst uvwxy z", True),
]


@pytest.mark.parametrize("sentence,expected", test_cases)
def test_check_if_pangram_user(sentence, expected):
    assert check_if_pangram_user(sentence) == expected


@pytest.mark.parametrize("sentence,expected", test_cases)
def test_check_if_pangram_canonical(sentence, expected):
    assert check_if_pangram_canonical(sentence) == expected
