**LeetCode #239**  
**Tags:** arrays, sliding window, heap, monotonic queue, deque

# Sliding Window Maximum

## Problem
Given an array of integers `nums` and an integer `k`, return the maximum value in each sliding window of size `k` as it moves from left to right across the array.

## Example
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               ---
[1 3 -1] -3  5  3  6  7         3
 1 [3 -1 -3] 5  3  6  7         3
 1  3 [-1 -3 5] 3  6  7         5
 1  3 -1 [-3 5 3] 6  7          5
 1  3 -1 -3 [5 3 6] 7           6
 1  3 -1 -3  5 [3 6 7]          7
```

## Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Clarifications & Assumptions
- The window moves one position at a time from left to right.
- The output array should have length `nums.length - k + 1`.
- If `k == 1`, the output is just the original array.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a deque for optimal performance.

## Notes
- Edge cases: k = 1, k = nums.length, all elements the same, negative numbers, strictly increasing/decreasing arrays. 