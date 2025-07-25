**LeetCode #15**  
**Tags:** array, two pointers, sorting

# 3Sum

## Problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

### Example 2
```
Input: nums = []
Output: []
```

### Example 3
```
Input: nums = [0]
Output: []
```

## Constraints
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Clarifications & Assumptions
- The solution set must not contain duplicate triplets.
- The order of the triplets in the output does not matter.
- Each triplet must have distinct indices.

## Approach
- Sort the array to make it easier to avoid duplicates and use two pointers.
- For each index i, use two pointers (left, right) to find pairs that sum to -nums[i], **only searching to the right of i (i.e., nums[i+1:])**.
- We do not search to the left of i, because this would generate duplicate triplets and violate the requirement for unique triplets with distinct, ordered indices.
- Skipping duplicate values for i, left, and right ensures all triplets are unique and no combination is revisited in a different order.
- Time complexity: O(n^2), space complexity: O(1) (not counting output).

## Notes
- Edge cases: empty array, all zeros, no solution, multiple duplicates.
- This is a classic interview problem testing array manipulation and two-pointer techniques. 