from .solution import longest_subarray_with_sum_at_most_k


def test_examples():
    test_cases = [
        ([1, 2, 3, 4, 5], 11, 4),
        ([2, 1, 5, 1, 3, 2], 7, 3),
        ([1, 1, 1, 1, 1], 3, 3),
    ]
    for nums, k, expected in test_cases:
        assert longest_subarray_with_sum_at_most_k(nums, k) == expected
