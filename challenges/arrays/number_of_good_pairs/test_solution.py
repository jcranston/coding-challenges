import pytest
from .solution import user_number_of_good_pairs, canonical_number_of_good_pairs


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([1], 0),
        ([1, 2, 1, 2, 1, 2], 6),
        ([100]*100, 4950),  # all the same
        (list(range(100)), 0),  # all unique
    ]
)
def test_number_of_good_pairs(nums, expected):
    for solution in [user_number_of_good_pairs, canonical_number_of_good_pairs]:
        assert solution(nums) == expected
