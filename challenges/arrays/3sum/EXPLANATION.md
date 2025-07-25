# Explanation: 3Sum (LeetCode 15)

## Problem Recap
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

## High-Level Approach
This problem is a classic example of using sorting and the two-pointer technique to efficiently find all unique triplets that sum to zero. The main challenge is to avoid duplicate triplets in the output.

## Step-by-Step Breakdown
1. **Sort the Array:**
   - Sorting helps to efficiently skip duplicates and use the two-pointer approach.
2. **Iterate with a Fixed Index:**
   - For each index `i` in `nums`, treat `nums[i]` as the first element of the triplet.
   - Skip duplicate values for `i` to avoid duplicate triplets.
3. **Two-Pointer Search:**
   - Use two pointers, `left` (i+1) and `right` (end), to find pairs such that `nums[i] + nums[left] + nums[right] == 0`.
   - If the sum is less than zero, move `left` forward. If greater, move `right` backward.
   - If a valid triplet is found, add it to the result and skip duplicates for both `left` and `right`.
4. **Continue Until All Triplets Are Found:**
   - Repeat for all valid `i`.

## Annotated Canonical Solution
```python
from typing import List

def canonical_three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate i
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1  # Skip duplicate left
                while left < right and nums[right] == nums[right+1]:
                    right -= 1  # Skip duplicate right
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```
- **Why this works:** Sorting and skipping duplicates ensures all triplets are unique. The two-pointer approach reduces the time complexity to O(n^2).

## Test Cases & Edge Cases
- `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
- `[]` → `[]`
- `[0]` → `[]`
- `[0,0,0]` → `[[0,0,0]]`
- `[1,2,-2,-1]` → `[]`
- `[0,0,0,0]` → `[[0,0,0]]`

## Common Pitfalls
- Not skipping duplicate values for `i`, `left`, or `right`, leading to duplicate triplets in the output.
- Not handling edge cases like empty arrays or arrays with fewer than three elements.
- Forgetting to sort the array before applying the two-pointer technique.

## Variations
- **k-Sum:** This approach generalizes to the k-Sum problem (e.g., 4Sum, kSum).
- **Target Sum:** Find triplets that sum to a target other than zero.
- **Return indices instead of values:** Some variants require returning the indices of the triplets.

## Relevant Literature
- [LeetCode 15: 3Sum](https://leetcode.com/problems/3sum/)
- [Two Pointer Technique - GeeksforGeeks](https://www.geeksforgeeks.org/two-pointer-technique/)
- [k-Sum Problem - Wikipedia](https://en.wikipedia.org/wiki/Subset_sum_problem)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 