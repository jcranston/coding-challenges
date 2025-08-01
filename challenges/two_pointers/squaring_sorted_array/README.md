**LeetCode #977: Squares of a Sorted Array**

**Tags:** array, two pointers, sorting

# Squares of a Sorted Array

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, return an array of the **squares of each number** sorted in non-decreasing order.

## Examples

**Example 1:**
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2:**
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Explanation: After squaring, the array becomes [49,9,4,9,121].
After sorting, it becomes [4,9,9,49,121].
```

**Example 3:**
```
Input: nums = [1,2,3,4,5]
Output: [1,4,9,16,25]
Explanation: After squaring, the array becomes [1,4,9,16,25].
After sorting, it becomes [1,4,9,16,25].
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Clarifications & Assumptions

- The input array is guaranteed to be sorted in non-decreasing order.
- The output should be sorted in non-decreasing order.
- Negative numbers when squared become positive, which can change the order.
- The array can contain negative numbers, zero, and positive numbers.
- The array can be empty (though constraints say minimum length is 1).
- You can use the same number multiple times if it appears multiple times in the input.

## Notes

- This is a classic problem that tests understanding of sorting and array manipulation.
- Consider what happens when you square different types of numbers.
- Think about how you can take advantage of the sorted nature of the input.
- The challenge is handling the transformation efficiently.
- Consider the relationship between the original array's structure and the final sorted result. 