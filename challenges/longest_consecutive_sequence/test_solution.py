import pytest

from .solution import (
    longest_consecutive_sequence_canonical,
    longest_consecutive_sequence_user,
)

test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([1, 2, 0, 1], 3),
    ([], 0),
    ([10], 1),
    ([1, 2, 2, 3], 3),
]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_longest_consecutive_sequence(nums, expected):
    for solution in [
        longest_consecutive_sequence_user,
        longest_consecutive_sequence_canonical,
    ]:
        assert solution(nums) == expected
