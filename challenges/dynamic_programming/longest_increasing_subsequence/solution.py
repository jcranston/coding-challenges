from typing import List, Tuple


def longest_increasing_subsequence_quadratic(
    nums: List[int],
) -> Tuple[int, List[int]]:
    """Returns the length and one actual longest increasing subsequence using
    O(n^2) DP."""
    if not nums:
        return 0, []
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_len = 1
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i
    # Reconstruct LIS
    lis = []
    idx = max_idx
    while idx != -1:
        lis.append(nums[idx])
        idx = prev[idx]
    lis.reverse()
    return max_len, lis


def longest_increasing_subsequence_optimized(
    nums: List[int],
) -> Tuple[int, List[int]]:
    """Returns the length and one actual longest increasing subsequence using
    O(n log n) method."""
    if not nums:
        return 0, []
    n = len(nums)
    tails = []  # stores indices
    prev = [-1] * n
    for i, num in enumerate(nums):
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if nums[tails[mid]] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(i)
        else:
            tails[left] = i
        prev[i] = tails[left - 1] if left > 0 else -1
    # Reconstruct LIS
    lis = []
    k = tails[-1]
    while k != -1:
        lis.append(nums[k])
        k = prev[k]
    lis.reverse()
    return len(tails), lis
