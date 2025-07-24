from collections import deque


def longest_subarray_with_sum_at_most_k(nums, k):
    """
    Canonical solution for finding the length of the longest contiguous subarray
    whose sum is less than or equal to k.
    Args:
        nums (List[int]): The list of integers.
        k (int): The maximum allowed sum for the subarray.
    Returns:
        int: The length of the longest such subarray, or 0 if none exists.
    """
    prefix_sums = [0]
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)

    q = deque()
    max_len = 0

    for j, curr_sum in enumerate(prefix_sums):
        while q and curr_sum - prefix_sums[q[0]] > k:
            q.popleft()
        if q:
            max_len = max(max_len, j - q[0])
        while q and prefix_sums[q[-1]] >= curr_sum:
            q.pop()
        q.append(j)
    return max_len
