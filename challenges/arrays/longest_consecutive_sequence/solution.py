from typing import List


def longest_consecutive_sequence_user(nums: List[int]) -> int:
    """User-submitted solution for finding the length of the longest consecutive
    sequence in an unsorted array.

    Args:
        nums (List[int]): The input array of integers.
    Returns:
        int: The length of the longest consecutive elements sequence.
    """
    numset = set(nums)
    if not nums:
        return 0
    max_streak = 1
    for num in numset:
        if num - 1 in numset:
            continue
        streak = 1
        next_num = num + 1
        while next_num in numset:
            streak += 1
            next_num += 1
        max_streak = max(max_streak, streak)
    return max_streak


def longest_consecutive_sequence_canonical(nums: List[int]) -> int:
    """Canonical solution for finding the length of the longest consecutive
    sequence in an unsorted array.

    Args:
        nums (List[int]): The input array of integers.
    Returns:
        int: The length of the longest consecutive elements sequence.
    """
    numset = set(nums)
    max_streak = 0
    for num in numset:
        if num - 1 in numset:
            continue
        streak = 1
        next_num = num + 1
        while next_num in numset:
            streak += 1
            next_num += 1
        max_streak = max(max_streak, streak)
    return max_streak
