**LeetCode #128**  
**Tags:** arrays, hash set, union find

# Longest Consecutive Sequence

## Problem
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Examples
- Input: nums = [100, 4, 200, 1, 3, 2]
  Output: 4
  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

- Input: nums = [0,3,7,2,5,8,4,6,0,1]
  Output: 9

## Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## Clarifications
- The sequence does not need to be contiguous in the array, but must be consecutive in value.
- Duplicates in the input array should be ignored for the purpose of the sequence.
- Return 0 if the array is empty. 