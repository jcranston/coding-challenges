import pytest

from .solution import contains_duplicate_canonical, contains_duplicate_user

test_cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([99], False),
    ([], False),
]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_contains_duplicate_user(nums, expected):
    assert contains_duplicate_user(nums) == expected


@pytest.mark.parametrize("nums,expected", test_cases)
def test_contains_duplicate_canonical(nums, expected):
    assert contains_duplicate_canonical(nums) == expected
