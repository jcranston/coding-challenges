# Subarray Sum Equals K

## Problem
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

## Clarifications & Constraints
- All values in `nums` are integers (can be negative, zero, or positive).
- The length of `nums` is between 1 and 20,000.
- The value of `k` is an integer and can be negative, zero, or positive.
- Subarrays must be continuous (no skipping elements).
- The same subarray can appear multiple times if it occurs at different positions.

## Example
Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation: The subarrays [1,2] and [3] both sum to 3.

## Approach
Consider using prefix sums and a hash map to efficiently count subarrays. Brute force is possible but not optimal for large arrays.

## Notes
- Watch for negative numbers and zero in the array.
- Think about edge cases: all zeros, all negatives, k = 0, etc. 