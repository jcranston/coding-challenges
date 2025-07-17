from .solution import (
    top_k_frequent_elements_canonical,
    top_k_frequent_elements_user,
)

test_cases = [
    # Example 1
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    # Example 2
    ([1], 1, [1]),
    # All unique
    ([4, 5, 6, 7], 2, [4, 5, 6, 7]),
    # All same
    ([2, 2, 2, 2], 1, [2]),
    # Negative numbers
    ([0, -1, -1, 2, 2, 2], 2, [2, -1, 0]),
]


def test_top_k_frequent_elements():
    for nums, k, expected in test_cases:
        for solution in [
            top_k_frequent_elements_user,
            top_k_frequent_elements_canonical,
        ]:
            result = solution(nums, k)
            # Check that result is a list of length k and contains the correct
            # elements
            assert len(result) == k
            for elem in result:
                assert elem in expected
