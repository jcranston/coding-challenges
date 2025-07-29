from typing import List


def kth_largest_element(nums: List[int], k):
    """Canonical solution for finding the k-th largest element in an array.

    Args:
        nums (List[int]): The list of integers.
        k (int): The k-th position to find (1-based).
    Returns:
        int: The k-th largest element in the array.
    """
    nums.sort()
    return nums[-k]
