from collections import Counter
from typing import List

def user_number_of_good_pairs(nums: List[int]) -> int:
    """
    User-submitted solution for LeetCode 1512: Number of Good Pairs.
    Args:
        nums: List of integers.
    Returns:
        The total number of good pairs (i, j) where nums[i] == nums[j] and i < j.
    """
    # Brute-force approach
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count

def canonical_number_of_good_pairs(nums: List[int]) -> int:
    """
    Canonical solution for LeetCode 1512: Number of Good Pairs.
    Args:
        nums: List of integers.
    Returns:
        The total number of good pairs (i, j) where nums[i] == nums[j] and i < j.
    """
    freq = Counter(nums)
    return sum(v * (v - 1) // 2 for v in freq.values())
