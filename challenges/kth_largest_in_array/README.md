# Kth Largest Element in an Array

## Problem
Given an integer array `nums` and an integer `k`, return the k-th largest element in the array.

**Note:** It is the k-th largest element in sorted order, not the k-th distinct element.

## Example
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Clarifications & Assumptions
- The input array may contain duplicates and negative numbers.
- The function should return an integer: the k-th largest element.
- k is always valid (1-based, and 1 <= k <= len(nums)).
- The array is not necessarily sorted.
- The answer is not required to be unique if there are duplicates.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a heap for optimal performance.

## Notes
- Edge cases: k = 1 (largest), k = len(nums) (smallest), all elements the same, negative numbers, duplicates. 