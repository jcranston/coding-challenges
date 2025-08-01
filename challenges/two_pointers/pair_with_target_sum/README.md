**LeetCode #167: Two Sum II - Input Array Is Sorted**

**Tags:** array, two pointers, binary search

# Two Sum II - Input Array Is Sorted

## Problem

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Examples

**Example 1:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated so that there is exactly one solution.

## Clarifications & Assumptions

- The array is 1-indexed, meaning the first element is at index 1, not 0.
- The array is guaranteed to be sorted in non-decreasing order.
- There is exactly one solution (no need to handle multiple solutions).
- You cannot use the same element twice.
- The solution must use only constant extra space (O(1) space complexity).
- The indices returned should be 1-indexed (add 1 to 0-indexed positions).

## Notes

- This is a classic problem that appears frequently in coding interviews.
- Think about how you can take advantage of the sorted nature of the array.
- Consider what happens when you compare elements from different ends of the array.
- The solution should be more efficient than the original Two Sum problem due to the sorted constraint. 