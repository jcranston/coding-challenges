**LeetCode #1512**  
**Tags:** array, hash table, counting

# Number of Good Pairs

Given an array of integers `nums`, return the number of good pairs.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

## Example
```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs: (0,3), (0,4), (3,4), (2,5)

Input: nums = [1,1,1,1]
Output: 6

Input: nums = [1,2,3]
Output: 0
```

## Constraints
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

## Clarifications & Assumptions
- The array may contain duplicate values.
- The function should return the total number of good pairs.

## Approach
- Use a hash table to count occurrences of each number.
- For each number, the number of good pairs is `count * (count - 1) // 2`.
- Sum over all numbers to get the total.

## Notes
- Edge cases: all unique, all the same, minimum/maximum length.
- Time complexity: O(n), where n is the length of nums.
- Space complexity: O(1) (since nums[i] is bounded). 