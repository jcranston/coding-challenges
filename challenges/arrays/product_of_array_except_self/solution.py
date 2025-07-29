def product_of_array_except_self(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i]
    is equal to the product of all the elements of nums except nums[i]. The
    solution must be done in O(n) time and without using division.

    Args:
        nums (list[int]): The input array of integers.
    Returns:
        list[int]: The product array as described.
    """
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output
