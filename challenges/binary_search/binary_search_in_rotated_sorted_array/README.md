# Binary Search in Rotated Sorted Array

## Problem
Given a rotated sorted array of distinct integers `nums` and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not in `nums`.

The array was originally sorted in ascending order and then rotated at some unknown pivot. (e.g., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You must write an algorithm with O(log n) runtime complexity.

## Example
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
```

## Constraints
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is guaranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4

## Clarifications & Assumptions
- The array contains no duplicate values.
- The array may not be rotated (i.e., it may be fully sorted).
- Return -1 if the target is not found.

## Approach
Describe your approach and thought process after attempting the problem. Consider using modified binary search for optimal performance.

## Notes
- Edge cases: array not rotated, target not present, single-element array, target at pivot, negative numbers. 