from typing import List


def find_minimum_in_rotated_sorted_array(nums: List[int]) -> int:
    """
    Returns the minimum element in a rotated sorted array.

    Args:
        nums: A list of unique integers representing a rotated sorted array.

    Returns:
        The minimum value in the array as an integer.

    Clarifications / Assumptions:
    - The input array is a rotated version of a sorted array (rotated between
      1 and n times).
    - All elements are unique.
    - The function should return the minimum value in the array as an integer.
    - The input array will always have at least one element.
    """
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
