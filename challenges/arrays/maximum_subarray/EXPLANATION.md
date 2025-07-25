# Maximum Subarray — EXPLANATION

## Problem Recap
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## High-Level Approach
Use Kadane's algorithm: iterate through the array, at each step decide whether to extend the current subarray or start a new one. Track the maximum sum found.

## Step-by-Step Solution
1. Initialize two variables: `max_sum` and `current_sum`, both set to the first element.
2. Iterate through the array starting from the second element:
    - For each number, set `current_sum` to the maximum of the current number or `current_sum + number`.
    - Update `max_sum` if `current_sum` is greater.
3. Return `max_sum`.

## Annotated Code
```python
from typing import List

def maximum_subarray(nums: List[int]) -> int:
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

## Example Test Cases
```python
assert maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6  # [4,-1,2,1]
assert maximum_subarray([1]) == 1
assert maximum_subarray([5,4,-1,7,8]) == 23
```

## Common Pitfalls
- Not handling all-negative arrays (the answer is the largest single element).
- Forgetting to initialize with the first element (not zero).
- Not updating the maximum at each step.

## Variations
- Return the actual subarray, not just its sum.
- Find the maximum product subarray.

## References
- [LeetCode #53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem) 