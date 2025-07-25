# Two Sum — EXPLANATION

## Problem Recap
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Each input has exactly one solution, and you may not use the same element twice.

## High-Level Approach
Use a hash table to store the indices of previously seen numbers. For each number, check if its complement (target - current number) has already been seen.

## Step-by-Step Solution
1. Initialize an empty dictionary to map numbers to their indices.
2. Iterate through the array:
    - For each number, compute its complement (target - number).
    - If the complement is in the dictionary, return the pair of indices.
    - Otherwise, store the current number and its index in the dictionary.
3. The problem guarantees exactly one solution, so you will always find a pair.

## Annotated Code
```python
from typing import List

def solve(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of the two numbers such that they add up to target.
    Assumes exactly one solution exists.
    """
    num_to_index = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], idx]
        num_to_index[num] = idx
    return []
```

## Example Test Cases
```python
assert solve([2, 7, 11, 15], 9) == [0, 1]
assert solve([3, 2, 4], 6) == [1, 2]
assert solve([3, 3], 6) == [0, 1]
```

## Common Pitfalls
- Using the same element twice (should not happen if you use indices correctly).
- Not handling negative numbers or zeros (the hash table approach works for all integers).
- Returning indices in the wrong order (the order does not matter unless specified).

## Variations
- Return the actual numbers instead of indices.
- Find all unique pairs that sum to the target (not just one).
- What if no solution exists? (Not allowed by this problem's constraints.)

## References
- [LeetCode #1: Two Sum](https://leetcode.com/problems/two-sum/)
- [Hash Table Pattern](https://leetcode.com/problems/two-sum/solutions/) 