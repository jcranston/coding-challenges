**LeetCode #209**  
**Tags:** arrays, sliding window, two pointers

# Minimum Size Subarray Sum

## Problem
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

## Example
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

## Clarifications & Assumptions
- All elements in nums are positive integers.
- The subarray must be contiguous.
- If no such subarray exists, return 0.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a sliding window for optimal performance.

## Notes
- Edge cases: no valid subarray, all elements >= target, target larger than sum of all elements, single-element array. 