from collections import defaultdict


def user_subarray_sum_equals_k(nums, k):
    """User-submitted solution for the Subarray Sum Equals K problem.

    Args:
        nums (List[int]): List of integers (can be negative, zero, or positive).
        k (int): Target sum for subarrays.
    Returns:
        int: Total number of continuous subarrays whose sum equals k.
    """
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    prefix_sum = 0
    total = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in prefix_sums:
            total += prefix_sums[prefix_sum - k]
        prefix_sums[prefix_sum] += 1

    return total


def canonical_subarray_sum_equals_k(nums, k):
    """Canonical solution for the Subarray Sum Equals K problem using prefix
    sums and a hash map.

    Args:
        nums (List[int]): List of integers (can be negative, zero, or positive).
        k (int): Target sum for subarrays.
    Returns:
        int: Total number of continuous subarrays whose sum equals k.
    """
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_sums[prefix_sum - k]
        prefix_sums[prefix_sum] += 1
    return count
