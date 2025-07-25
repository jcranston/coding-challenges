# Longest Consecutive Sequence — EXPLANATION

## Problem Recap
Given an unsorted array of integers, return the length of the longest consecutive elements sequence. The sequence does not need to be contiguous in the array, but must be consecutive in value. The algorithm must run in O(n) time.

## High-Level Approach
Use a hash set to allow O(1) lookups. For each number, only start counting a sequence if it is the start of a sequence (i.e., num - 1 is not in the set). Expand forward to count the length of the sequence.

## Step-by-Step Solution
1. Add all numbers to a set for O(1) lookups.
2. For each number in the set:
    - If num - 1 is not in the set, this is the start of a sequence.
    - Expand forward (num + 1, num + 2, ...) as long as the next number is in the set, counting the streak.
    - Track the maximum streak found.
3. Return the maximum streak length.

## Annotated Code
```python
from typing import List

def longest_consecutive_sequence(nums: List[int]) -> int:
    numset = set(nums)
    max_streak = 0
    for num in numset:
        if num - 1 in numset:
            continue  # not the start of a sequence
        streak = 1
        next_num = num + 1
        while next_num in numset:
            streak += 1
            next_num += 1
        max_streak = max(max_streak, streak)
    return max_streak
```

## Example Test Cases
```python
assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4  # [1,2,3,4]
assert longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]) == 9
assert longest_consecutive_sequence([]) == 0
```

## Common Pitfalls
- Not checking for the start of a sequence (can lead to O(n^2) time).
- Not handling empty arrays (should return 0).
- Counting duplicates (should be ignored by using a set).

## Variations
- Return the actual sequence, not just its length.
- Find the longest increasing (not necessarily consecutive) subsequence.

## References
- [LeetCode #128: Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [Hash Set Pattern](https://leetcode.com/problems/longest-consecutive-sequence/solutions/) 