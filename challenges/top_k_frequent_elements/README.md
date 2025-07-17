# Top K Frequent Elements

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Example
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

## Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in nums]
- It is guaranteed that the answer is unique

## Clarifications & Assumptions
- The returned list can be in any order.
- If multiple elements have the same frequency, any subset of them can be returned as long as the total is k.
- The function should return a list of integers of length k.
- The input array may contain negative numbers and zeros.

## Input Format
- The function will receive two arguments:
    - `nums` (List[int]): the input array
    - `k` (int): the number of most frequent elements to return

## Output Format
- Return a list of k integers: the k most frequent elements in any order.

## Notes
- Consider using a hash map to count frequencies and a heap or bucket sort to find the top k elements efficiently.
- Edge cases: all elements unique, all elements the same, k = 1, k = len(nums), negative numbers. 