# Explanation: Contains Duplicate (LeetCode 217)

## Problem Recap
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Approach
The most efficient way to check for duplicates in an array is to use a hash set:
- Iterate through each number in the array.
- For each number, check if it is already in the set.
  - If it is, return True (duplicate found).
  - If not, add it to the set.
- If the loop completes, return False (no duplicates).

This approach leverages the O(1) average time complexity for set lookups and insertions in Python.

## Code Reasoning
- The set keeps track of all unique numbers seen so far.
- As soon as a duplicate is found, the function returns early for efficiency.
- This avoids the O(n^2) time complexity of comparing every pair.

## Edge Cases
- Empty array: returns False (no elements, so no duplicates).
- Array of one element: returns False.
- Array with all unique elements: returns False.
- Array with all elements the same: returns True.

## Why Use a Set?
- Sets provide O(1) average time complexity for add and lookup.
- Using a list would result in O(n) lookup, making the overall time O(n^2).

## Related Literature
- This is a classic use of hash sets for duplicate detection, discussed in most introductory data structures and algorithms textbooks (e.g., CLRS, Chapter 10).
- LeetCode Discuss: [Contains Duplicate - HashSet Solution](https://leetcode.com/problems/contains-duplicate/solutions/61609/a-simple-hashset-solution/)

## Invariants
- At each step, the set contains all unique elements seen so far.
- The function returns as soon as a duplicate is found, ensuring minimal work.

## Code Example
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
``` 