from .solution import (
    canonical_subarray_sum_equals_k,
    user_subarray_sum_equals_k,
)


def test_subarray_sum_equals_k():
    nums = [1, 2, 3]
    k = 3
    expected = 2  # [1,2] and [3]
    for solution in [
        user_subarray_sum_equals_k,
        canonical_subarray_sum_equals_k,
    ]:
        assert solution(nums, k) == expected
