# Find the Duplicate Number — EXPLANATION

## Problem Recap
Given an array of n + 1 integers where each integer is between 1 and n (inclusive), and only one duplicate number exists, return the duplicate. The solution must not modify the array and must use O(1) extra space.

## High-Level Approach
Use Floyd's Tortoise and Hare (cycle detection) algorithm to find the duplicate. Treat the array as a linked list where each value points to the next index, and the duplicate forms a cycle.

## Step-by-Step Solution
1. Initialize two pointers, `slow` and `fast`, both at the start of the array.
2. Move `slow` by one step and `fast` by two steps until they meet (detect cycle).
3. Reset one pointer to the start. Move both pointers one step at a time until they meet again; this meeting point is the duplicate number.

## Annotated Code
```python
def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    # Phase 1: Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: Find entrance to the cycle
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow
```

## Example Test Cases
```python
assert find_duplicate([1,3,4,2,2]) == 2
assert find_duplicate([3,1,3,4,2]) == 3
```

## Common Pitfalls
- Modifying the array (not allowed).
- Using extra space (hash set or array) — not O(1) space.
- Not understanding why the cycle detection works (see detailed math explanation below).

## Variations
- Find all duplicates (not just one).
- Array may contain multiple duplicates.

## References
- [LeetCode #287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- See also: `Floyds_Tortoise_and_Hare_Explanation.md` in this directory for a detailed mathematical proof and visualization of why the pointers meet at the cycle start. 