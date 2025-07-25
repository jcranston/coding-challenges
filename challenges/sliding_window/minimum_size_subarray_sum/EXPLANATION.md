# Explanation: Minimum Size Subarray Sum

## Problem Recap
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return 0.

## High-level Approach
A brute-force approach would check all possible subarrays, but this is inefficient for large arrays. The optimal solution uses a sliding window to efficiently find the minimal-length subarray in O(n) time.

## Step-by-step Breakdown
1. **Sliding Window:**
   - Use two pointers (`left` and `right`) to represent the current window.
   - Expand the window by moving `right` and adding `nums[right]` to the running sum.
   - When the sum is greater than or equal to `target`, try to shrink the window from the left to find the minimal length.
2. **Update Result:**
   - Whenever a valid window is found, update the minimal length and record the subarray.
   - Continue until the end of the array.
3. **Result:**
   - If no valid window is found, return 0 and an empty list. Otherwise, return the minimal length and the subarray.

## Annotated Code (User Solution)
```python
def minimum_size_subarray_sum(target, nums):
    if not nums:
        return (0, [])
    n = len(nums)
    l_min, r_min = 0, 0
    l, r = 0, 0
    rolling_sum = 0
    smallest_window = float("inf")
    while r < n:
        while rolling_sum < target and r <= n - 1:
            rolling_sum += nums[r]
            r += 1
        while rolling_sum >= target and l < r:
            rolling_sum -= nums[l]
            l += 1
        if l == 0 and r == n and rolling_sum < target:
            return (0, [])
        window_len = r - l + 1
        if window_len < smallest_window:
            smallest_window = window_len
            l_min = l - 1
            r_min = r - 1
    return (
        (0, [])
        if smallest_window == float("inf")
        else (smallest_window, nums[l_min : r_min + 1])
    )
```
- The window is expanded and contracted to always maintain the minimal valid window.
- Time complexity is O(n), where n is the length of `nums`.

## Test Cases
- `target = 7, nums = [2, 3, 1, 2, 4, 3]` → Output: `(2, [4, 3])`
- `target = 4, nums = [1, 4, 4]` → Output: `(1, [4])`
- `target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]` → Output: `(0, [])`
- `target = 15, nums = [1, 2, 3, 4, 5]` → Output: `(5, [1, 2, 3, 4, 5])`

## Common Pitfalls
- Not shrinking the window from the left after reaching the target sum.
- Not handling the case where no valid subarray exists.
- Off-by-one errors in window indices.

## Variations
- If negative numbers are allowed, a different approach is needed.
- If you want the maximum sum with a length constraint, adjust the window logic.

## Relevant Literature
- [LeetCode #209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [Sliding Window Technique](https://leetcode.com/tag/sliding-window/)
- CLRS, Section 10.1: Queues 