# Explanation: Number of Good Pairs (LeetCode 1512)

## Problem Recap
Given an array of integers `nums`, return the number of good pairs. A pair `(i, j)` is good if `nums[i] == nums[j]` and `i < j`.

## High-Level Approach
Count how many times each number appears. For each number, the number of good pairs is `count * (count - 1) // 2`. Sum these for all numbers.

## Annotated Canonical Solution
```python
from collections import Counter

def canonical_number_of_good_pairs(nums):
    freq = Counter(nums)
    return sum(v * (v - 1) // 2 for v in freq.values())
```
- This uses a hash table to count occurrences and computes the number of pairs for each value.

## Test Cases & Edge Cases
- `[1,2,3,1,1,3]` → `4`
- `[1,1,1,1]` → `6`
- `[1,2,3]` → `0`
- `[1]` → `0`
- `[100]*100` → `4950`

## Common Pitfalls
- Forgetting to check `i < j` (the formula handles this).
- Not handling arrays with all unique or all identical elements.

## Relevant Literature
- [LeetCode 1512: Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

---
This explanation is concise due to the simplicity of the problem, as recommended in `ai_context/explanation_generation.md`. 