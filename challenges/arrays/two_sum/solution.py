from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    """Returns indices of the two numbers such that they add up to target.

    Assumes exactly one solution exists.
    """
    num_to_index = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], idx]
        num_to_index[num] = idx
    return []
