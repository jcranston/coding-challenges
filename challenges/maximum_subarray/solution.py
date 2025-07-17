from typing import List, Tuple


def max_subarray_with_indices(nums: List[int]) -> Tuple[int, List[int]]:
    """
    Returns the maximum sum of a contiguous subarray and the subarray itself.
    """
    if not nums:
        return 0, []

    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start : end + 1]
