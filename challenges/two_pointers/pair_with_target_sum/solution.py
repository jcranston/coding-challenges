"""
Two Sum II - Input Array Is Sorted

LeetCode #167
LeetCode Problem: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as
an integer array [index1, index2] of length 2.
"""


def two_sum_sorted_user(numbers: list[int], target: int) -> list[int]:
    """Find two numbers in the sorted array that add up to the target.

    Args:
        numbers: Sorted array of integers (1-indexed)
        target: Target sum to find

    Returns:
        List containing the two indices (1-indexed) that sum to target
    """
    left, right = 0, len(numbers) - 1
    sum = numbers[left] + numbers[right]

    while sum > target:
        right -= 1
        sum = numbers[left] + numbers[right]

    while sum < target:
        left += 1
        sum = numbers[left] + numbers[right]

    return [left + 1, right + 1]


def two_sum_sorted_canonical(numbers: list[int], target: int) -> list[int]:
    """Find two numbers in the sorted array that add up to the target.

    Uses two pointers technique since the array is sorted.

    Args:
        numbers: Sorted array of integers (1-indexed)
        target: Target sum to find

    Returns:
        List containing the two indices (1-indexed) that sum to target
    """
    if not numbers or len(numbers) < 2:
        return []

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need a larger sum, move left pointer right
            left += 1
        else:
            # Need a smaller sum, move right pointer left
            right -= 1

    # No solution found (though problem guarantees one exists)
    return []
