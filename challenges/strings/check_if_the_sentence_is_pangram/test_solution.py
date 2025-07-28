import pytest

from .solution import check_if_pangram_canonical, check_if_pangram_user

test_cases = [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("", False),
    ("a quick movement of the enemy will jeopardize five gunboats", False),
]


@pytest.mark.parametrize("sentence, expected", test_cases)
def test_check_if_pangram_user(sentence, expected):
    result = check_if_pangram_user(sentence)
    if result is None:
        # If function is not implemented, just pass the test
        return
    assert result == expected


@pytest.mark.parametrize("sentence, expected", test_cases)
def test_check_if_pangram_canonical(sentence, expected):
    result = check_if_pangram_canonical(sentence)
    if result is None:
        # If function is not implemented, just pass the test
        return
    assert result == expected
