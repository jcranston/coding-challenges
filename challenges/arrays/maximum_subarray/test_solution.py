from .solution import max_subarray_with_indices


def test_example():
    # Example: nums = [-2,1,-3,4,-1,2,1,-5,4]; Output: 6
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = (6, [4, -1, 2, 1])
    assert max_subarray_with_indices(nums) == expected
