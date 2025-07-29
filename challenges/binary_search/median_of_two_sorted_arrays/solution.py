from math import floor
from typing import List


def median_of_two_sorted_arrays_user(
    nums1: List[int], nums2: List[int]
) -> float:
    """User implementation for finding the median of two sorted arrays.

    Take i elems from nums1 and j elems from nums2 such that
    i + j = (m + n + 1) // 2

    Assuming array a is smaller of the two and b is the larger,
    need to find i such that a[i - 1] <= b[j]
    (largest on the left of a <= smallest from the right of b)
    and...
    b[j - 1] <= a[i]
    (largest on the left from b <= smallest from the right of a)
    """
    # array a is smaller (length m) or equal to array b (length n)
    if len(nums1) <= len(nums2):
        a, b = nums1, nums2
    else:
        a, b = nums2, nums1
    m, n = len(a), len(b)

    # perform binary search on smaller array
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return max(a_left, b_left)
            else:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1


def median_of_two_sorted_arrays_canonical(
    nums1: List[int], nums2: List[int]
) -> float:
    """Canonical solution for finding the median of two sorted arrays."""
    pass
