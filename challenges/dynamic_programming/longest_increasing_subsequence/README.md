**LeetCode #300**  
**Tags:** dynamic programming, binary search

# Longest Increasing Subsequence

## Problem Description

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples

### Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

### Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

### Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Clarifications

- A subsequence does not need to be contiguous
- The subsequence must be strictly increasing (no equal elements)
- If all elements are equal, the longest increasing subsequence has length 1
- The order of elements in the original array must be preserved in the subsequence
- You only need to return the length, not the actual subsequence

## Approach Hints

1. **Dynamic Programming**: Consider using a DP array where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`
2. **Binary Search Optimization**: For an O(n log n) solution, maintain a sorted array of the smallest tail values for each length
3. **Greedy with Binary Search**: Keep track of the smallest possible tail value for each subsequence length

## Follow-up Questions

- Can you find the actual subsequence, not just its length?
- What if we want to find the longest decreasing subsequence?
- How would you modify the solution to handle duplicate elements differently? 