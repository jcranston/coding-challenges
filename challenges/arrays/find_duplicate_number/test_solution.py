from .solution import (
    canonical_find_duplicate_number,
    user_find_duplicate_number,
)


def test_find_duplicate_number():
    # Example test case
    nums = [1, 3, 4, 2, 2]
    expected = 2
    for solution in [
        user_find_duplicate_number,
        canonical_find_duplicate_number,
    ]:
        assert solution(nums) == expected
