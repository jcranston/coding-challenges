# Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the rotated array `nums`, return the minimum element of this array.

## Example

```
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

Input: nums = [11,13,15,17]
Output: 11
```

## Constraints
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is guaranteed to be rotated at least once.

## Clarifications / Assumptions
- The input array is a rotated version of a sorted array (rotated between 1 and n times).
- All elements are unique.
- The function should return the minimum value in the array as an integer.
- The input array will always have at least one element. 